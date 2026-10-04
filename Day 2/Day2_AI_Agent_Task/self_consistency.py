"""
Day 2 Task - Self-Consistency

This script demonstrates the idea of self-consistency by generating
multiple reasoning variations and finding the majority answer.

Note:
This is a local simulation because no LLM API is being used.
"""

import random


def generate_answer(temperature):
    """
    Simulate different reasoning outputs.

    temperature = 0:
        Always produces the same deterministic answer.

    temperature > 0:
        Allows small variation between candidate answers.
    """

    correct_answer = "Math Assignment"

    if temperature == 0:
        return correct_answer

    # Simulate variation at non-zero temperature
    possible_answers = [
        "Math Assignment",
        "Math Assignment",
        "Math Assignment",
        "DBMS Assignment"
    ]

    return random.choice(possible_answers)


def self_consistency():
    print("=== SELF-CONSISTENCY ===")

    question = (
        "Which assignment should I complete first, "
        "and why?"
    )

    print("\nQuestion:")
    print(question)

    # Non-zero temperature simulation
    temperature = 0.7
    number_of_runs = 5

    print(
        f"\nRunning {number_of_runs} times "
        f"with simulated temperature = {temperature}"
    )

    answers = []

    for i in range(number_of_runs):
        answer = generate_answer(temperature)
        answers.append(answer)
        print(f"Run {i + 1}: {answer}")

    # Count answers
    counts = {}

    for answer in answers:
        counts[answer] = counts.get(answer, 0) + 1

    majority_answer = max(
        counts,
        key=counts.get
    )

    print("\nAnswer Counts:")

    for answer, count in counts.items():
        print(f"{answer}: {count}")

    print("\nMajority Answer:")
    print(majority_answer)

    print("\nCorrect Answer:")
    print("Math Assignment")

    if majority_answer == "Math Assignment":
        print("Result: Majority answer is correct.")
    else:
        print("Result: Majority answer is incorrect.")

    # Temperature 0
    print("\nTemperature = 0")

    deterministic_answers = []

    for i in range(3):
        answer = generate_answer(0)
        deterministic_answers.append(answer)
        print(f"Run {i + 1}: {answer}")

    print(
        "\nObservation:"
        "\nAt temperature 0, the output remains deterministic "
        "and consistent across runs."
    )

    print(
        "\nLimitation:"
        "\nThis experiment simulates temperature-based variation "
        "locally. It does not use an actual LLM API."
    )


if __name__ == "__main__":
    self_consistency()