"""Day 6: the Day 3 agent, ported to the OpenAI-compatible API,
with validation and retry.
"""

import json

from config import client, MODEL, banner
from tools_v2 import TOOLS, TOOL_FUNCTIONS, SCHEMAS
from validate import validate_arguments


SYSTEM_PROMPT = (
    "You are a college fee assistant. Never guess a fee: always call "
    "get_course_fee. Use calculator for every arithmetic step. "
    "Valid course codes: CS101, AI202, DS303. "
    "If no tool is needed, answer directly."
)

MAX_TOKENS = 500
REPEAT_LIMIT = 3


def handle_tool_call(call, log=True):
    """Run one tool call defensively. Always returns a string for the model."""

    name = call.function.name
    raw = call.function.arguments or "{}"

    # 1. Arguments are generated text and may not be valid JSON
    try:
        arguments = json.loads(raw)
    except json.JSONDecodeError as error:
        return (
            f"Argument error: invalid JSON ({error}). "
            f"Send valid JSON for '{name}'."
        )

    # 2. The tool may not exist
    function = TOOL_FUNCTIONS.get(name)

    if function is None:
        return (
            f"Unknown tool: {name}. "
            f"Available tools: {', '.join(TOOL_FUNCTIONS)}."
        )

    # 3. Arguments may not match the schema
    problem = validate_arguments(arguments, SCHEMAS[name])

    if problem:
        return f"Argument error: {problem}"

    # 4. The tool itself may fail
    try:
        result = str(function(**arguments))
    except Exception as error:
        result = (
            f"Tool error in {name}: "
            f"{type(error).__name__}: {error}"
        )

    if log:
        print(
            f"          {name}({arguments}) -> "
            f"{result[:100]}"
        )

    return result


def agent(question, max_steps=6, verbose=True):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]

    seen = {}
    max_tokens = MAX_TOKENS

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0,
            max_tokens=max_tokens
        )

        choice = response.choices[0]
        message = choice.message

        # Retry if the response was truncated
        if choice.finish_reason == "length":
            if max_tokens >= 2000:
                return "Stopped: the reply was still truncated at 2000 tokens."

            max_tokens *= 2

            if verbose:
                print(
                    f"   step {step}: truncated, "
                    f"retrying with max_tokens={max_tokens}"
                )

            continue

        # No tool call means the model has produced its final answer
        if not message.tool_calls:
            return (message.content or "").strip()

        # Add assistant tool-call message
        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": c.id,
                    "type": "function",
                    "function": {
                        "name": c.function.name,
                        "arguments": c.function.arguments
                    }
                }
                for c in message.tool_calls
            ]
        })

        if verbose:
            print(
                f"   step {step}: "
                f"{len(message.tool_calls)} tool call(s)"
            )

        # Handle every tool call
        for call in message.tool_calls:

            signature = (
                call.function.name,
                call.function.arguments
            )

            seen[signature] = seen.get(signature, 0) + 1

            # Stop repeated identical failing calls
            if seen[signature] >= REPEAT_LIMIT:
                return (
                    f"Stopped: {call.function.name} was called "
                    f"{REPEAT_LIMIT} times with the same arguments "
                    f"and made no progress."
                )

            result = handle_tool_call(
                call,
                log=verbose
            )

            # Exactly one tool message per tool_call_id
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    return "Stopped: maximum steps reached without a final answer."


if __name__ == "__main__":

    banner("ROBUST AGENT")

    for question in [
        "What is the total fee for CS101 and AI202 after a 10% scholarship?",
        "Is DS303 more expensive than CS101, and by how much?",
        "What is the fee for ME404?",
        "Write a one-line welcome message for new students."
    ]:

        print("\nQ:", question)
        print("A:", agent(question))