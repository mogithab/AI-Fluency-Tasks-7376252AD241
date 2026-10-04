from datetime import datetime


def get_current_date():
    """Tool to get the current date."""
    return datetime.now().strftime("%d-%m-%Y")


def get_assignment_data():
    """Tool to retrieve student assignment information."""
    return [
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


def get_external_information():
    """Simulates an external information source used by the ReAct agent."""
    return {
        "current_date": get_current_date(),
        "assignments": get_assignment_data()
    }


if __name__ == "__main__":
    information = get_external_information()

    print("=== EXTERNAL TOOL RESULT ===")
    print("Current Date:", information["current_date"])
    print("\nAssignments:")

    for item in information["assignments"]:
        print(
            f"{item['subject']} | "
            f"{item['assignment']} | "
            f"Deadline: {item['deadline']} | "
            f"Status: {item['status']}"
        )