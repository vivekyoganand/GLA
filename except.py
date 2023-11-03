Exception Handling in Python:

In Python, exception handling is the process of managing runtime errors gracefully. It involves using the following keywords and constructs:

try: This block is used to enclose code that may raise an exception.
except: This block catches and handles exceptions that occur in the try block.
else: This block is executed if no exception occurs in the try block.
finally: This block always runs, regardless of whether an exception was raised or not.
raise: This statement is used to raise custom exceptions.


Division by Zero
==
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Cannot divide by zero"
    return result

numerator = 10
denominator = 0
result = divide(numerator, denominator)
print(f"Result: {result}")

Output
==
Result: Cannot divide by zero

 File Handling
 ==
 try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    content = "File not found"
finally:
    print(f"File content: {content}")

Output
==
File content: File not found

Custom Exception
==
class CustomError(Exception):
    pass

def custom_exception_example(value):
    try:
        if value < 0:
            raise CustomError("Value should be positive")
    except CustomError as e:
        print(f"Custom Error: {e}")
    else:
        print("No custom error occurred")

custom_exception_example(-5)

Output
==
Custom Error: Value should be positive

Index Out of Range
==
try:
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError:
    print("Index out of range")

Output
==
Index out of range

Input Validation
==
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Your age is {age}")

Negative Age
==
Enter your age: -5
Error: Age cannot be negative


