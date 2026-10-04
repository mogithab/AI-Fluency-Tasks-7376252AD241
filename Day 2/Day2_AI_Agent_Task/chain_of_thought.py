"""
Day 2 Task - Chain-of-Thought

This is a simplified reasoning trace for demonstration.
It shows the main decision steps without exposing private model reasoning.
"""

assignments = [
    {
        "subject": "Mathematics",
        "assignment": "Math Assignment",
        "deadline": "25-09-2026",
        "status": "Pending"
    },
    {
        "subject": "DBMS",
        "assignment": "DBMS Assignment",
        "deadline": "27-09-2026",
        "status": "Pending"
    },
    {
        "subject": "Artificial Intelligence",
        "assignment": "AI Assignment",
        "deadline": "30-09-2026",
        "status": "Pending"
    }
]


def chain_of_thought():
    print("=== CHAIN-OF-THOUGHT ===")

    print("\nQuestion:")
    print("Which assignment should I complete first, and why?")

    print("\nSimplified Reasoning Steps:")

    print("Step 1: Check the deadlines of all pending assignments.")

    print("Step 2: Compare the deadlines:")
    for item in assignments:
        print(
            f"  {item['assignment']} -> {item['deadline']}"
        )

    print("Step 3: Identify the earliest deadline.")

    earliest = min(
        assignments,
        key=lambda x: tuple(map(int, x["deadline"].split("-")[::-1]))
    )

    print(
        f"Step 4: The earliest deadline is "
        f"{earliest['deadline']}."
    )

    print("\nAnswer:")
    print(
        f"Complete the {earliest['assignment']} first because "
        f"it has the earliest deadline."
    )

    print("\nLimitation:")
    print(
        "Chain-of-thought can break a problem into multiple reasoning "
        "steps, but it cannot obtain new external information by itself."
    )


if __name__ == "__main__":
    chain_of_thought()