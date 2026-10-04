print("=== RULE-BASED WORKFLOW ===")

question = input("Ask your question: ").lower()

if "mathematics" in question and "deadline" in question:
    print("\nWorkflow:")
    print("Mathematics assignment deadline: 25 September 2026")

elif "dbms" in question and "deadline" in question:
    print("\nWorkflow:")
    print("DBMS assignment deadline: 27 September 2026")

elif "marks" in question:
    print("\nWorkflow:")
    print("Data Structures: 85")
    print("Mathematics: 78")
    print("Artificial Intelligence: 88")
    print("DBMS: 82")

else:
    print("\nWorkflow:")
    print("No predefined rule found.")