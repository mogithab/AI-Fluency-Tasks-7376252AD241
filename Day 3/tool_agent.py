# Tool-enabled agent
# This script uses an external tool to retrieve information
# and perform a calculation.

from tools import get_course_fee, calculator


# Function that uses tools to answer the question
def answer_with_tool():
    print("=== TOOL-ENABLED AGENT ===")

    # Step 1: Call the course-fee tool
    cs_fee = get_course_fee("CS101")
    ai_fee = get_course_fee("AI202")

    print("Tool call 1: get_course_fee('CS101')")
    print("Result:", cs_fee)

    print("Tool call 2: get_course_fee('AI202')")
    print("Result:", ai_fee)

    # Step 2: Calculate the total fee
    total = calculator(f"{cs_fee} + {ai_fee}")

    print("Tool call 3: calculator(...)")
    print("Result:", total)

    # Step 3: Apply the 10% merit scholarship
    final_fee = calculator(f"{total} * 0.9")

    print("Tool call 4: calculator(...)")
    print("Result:", final_fee)

    # Final answer
    print()
    print("Final Answer:")
    print(
        f"CS101 + AI202 total fee after 10% scholarship = Rs. {final_fee}"
    )


# Run the agent
if __name__ == "__main__":
    answer_with_tool()