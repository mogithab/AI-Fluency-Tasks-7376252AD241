# No-tool LLM-style script
# This script answers using only information already known in the prompt.
# It does not call any external tool.

def answer_without_tool(question):
    # Example response based only on the information given
    if "what is an llm" in question.lower():
        return "An LLM is a Large Language Model that can understand and generate text."

    if "capital of india" in question.lower():
        return "The capital of India is New Delhi."

    return "I can answer this using the information available in my prompt."


# Questions to demonstrate answers without using a tool
questions = [
    "What is an LLM?",
    "What is the capital of India?"
]

# Display the questions and answers
for question in questions:
    print("Q:", question)
    print("A:", answer_without_tool(question))
    print()