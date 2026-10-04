# Function to get the fee of a course using its course code
def get_course_fee(course_code):

    # Store course codes and their fees in a dictionary
    fees = {
        "CS101": 12000,
        "AI202": 18000,
        "DS303": 15000
    }

    # Check whether the given course code exists
    if course_code in fees:

        # Return the fee of the requested course
        return fees[course_code]

    # Return None if the course code is not found
    return None


# Function to perform a calculation
def calculator(expression):

    try:
        # Evaluate the mathematical expression
        # __builtins__ is disabled to make eval safer
        return eval(expression, {"__builtins__": {}}, {})

    except Exception as e:
        # Return an error message if the calculation fails
        return f"Calculation error: {e}"


# This code runs only when tools.py is executed directly
if __name__ == "__main__":

    # Test the course-fee tool
    print("CS101 fee:", get_course_fee("CS101"))

    # Test the calculator tool
    print("Total:", calculator("12000 + 18000"))