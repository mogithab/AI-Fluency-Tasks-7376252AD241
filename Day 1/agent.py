print("=== AI AGENT ===")

def read_private_data():
    print("Tool: Reading private student data...")
    
    with open("student_data.txt", "r") as file:
        return file.read()


question = input("Ask the agent: ")

print("\nAgent:")
print("Step 1: Understanding the question")

data = read_private_data()

print("Step 2: Observing private data")
print("Step 3: Finding the required information")
print("Step 4: Generating final answer")

if "mathematics" in question.lower() and "deadline" in question.lower():
    print("\nFinal Answer:")
    print("Mathematics assignment deadline: 25 September 2026")

elif "dbms" in question.lower() and "deadline" in question.lower():
    print("\nFinal Answer:")
    print("DBMS assignment deadline: 27 September 2026")

else:
    print("\nFinal Answer:")
    print("I found the private data but could not answer this question.")