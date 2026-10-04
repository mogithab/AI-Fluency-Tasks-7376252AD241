"""
Day 2 Task - Direct Prompting

Direct prompting gives the model a question and asks for an answer
directly, without using external tools.
"""

from datetime import datetime


# Information already available to the model
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


def direct_prompt():
    print("=== DIRECT PROMPTING ===")

    print("\nQuestion:")
    print(
        "Which assignment should I complete first, "
        "and why?"
    )

    print("\nAnswer:")
    print(
        "You should complete the Mathematics assignment first "
        "because it has the earliest deadline, 25-09-2026. "
        "The DBMS assignment is due on 27-09-2026, followed by "
        "the Artificial Intelligence assignment on 30-09-2026."
    )

    print("\nLimitation:")
    print(
        "Direct prompting answers immediately from the information "
        "available to the model. It does not use an external tool "
        "to obtain new information."
    )


if __name__ == "__main__":
    direct_prompt()