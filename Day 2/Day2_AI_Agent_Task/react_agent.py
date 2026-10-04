"""
Day 2 Task - ReAct Agent

ReAct combines reasoning with actions.
The agent uses an external tool to obtain current information.
"""

from tools import get_external_information


def react_agent():
    print("=== ReACT AGENT ===")

    print("\nQuestion:")
    print(
        "Which assignment should I complete first, "
        "and what is the current date?"
    )

    # Thought
    print("\nThought:")
    print(
        "I need the current date and assignment information "
        "before deciding which assignment should be completed first."
    )

    # Action
    print("\nAction:")
    print("Calling external tool: get_external_information()")

    information = get_external_information()

    # Observation
    print("\nObservation:")
    print("Current Date:", information["current_date"])

    print("\nAssignment Data:")
    for item in information["assignments"]:
        print(
            f"{item['subject']} | "
            f"{item['assignment']} | "
            f"Deadline: {item['deadline']} | "
            f"Status: {item['status']}"
        )

    # Reasoning using obtained information
    pending_assignments = [
        item
        for item in information["assignments"]
        if item["status"] == "Pending"
    ]

    earliest = min(
        pending_assignments,
        key=lambda x: tuple(
            map(int, x["deadline"].split("-")[::-1])
        )
    )

    # Final answer
    print("\nFinal Answer:")
    print(
        f"Today is {information['current_date']}. "
        f"You should complete the {earliest['assignment']} first "
        f"because it has the earliest deadline, "
        f"{earliest['deadline']}."
    )

    print("\nLimitation:")
    print(
        "ReAct depends on external tools or information sources. "
        "If the tool provides incorrect or unavailable information, "
        "the final answer may also be affected."
    )


if __name__ == "__main__":
    react_agent()