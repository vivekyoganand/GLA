Python Each program is followed by its output:

1. Local Variable Scope:
python
Copy code
def local_variable_demo():
    x = 10  # Local variable
    print("Inside the function, x =", x)

local_variable_demo()
# Attempting to access x outside the function will result in an error
Output:

bash
Copy code
Inside the function, x = 10
2. Global Variable Scope:
python
Copy code
global_variable = 20  # Global variable

def access_global_variable():
    print("Accessing the global variable:", global_variable)

access_global_variable()
Output:

csharp
Copy code
Accessing the global variable: 20
3. Modifying Global Variable:
python
Copy code
global_variable = 20  # Global variable

def modify_global_variable():
    global global_variable
    global_variable = 30

modify_global_variable()
print("Global variable after modification:", global_variable)
Output:

sql
Copy code
Global variable after modification: 30
4. Non-Local Variable Scope:
python
Copy code
def outer_function():
    outer_variable = 5

    def inner_function():
        nonlocal outer_variable
        outer_variable = 10

    inner_function()
    print("Outer variable (non-local):", outer_variable)

outer_function()
Output:

sql
Copy code
Outer variable (non-local): 10
5. Using Anonymous (Lambda) Functions:
python
Copy code
# Lambda function to add two numbers
add = lambda x, y: x + y
result = add(3, 4)
print("Result of adding 3 and 4:", result)

# Lambda function to find the square of a number
square = lambda x: x ** 2
num = 5
print("Square of", num, "is", square(num))
Output:

csharp
Copy code
Result of adding 3 and 4: 7
Square of 5 is 25
6. Local Variable Shadowing:
python
Copy code
x = 20  # Global variable

def local_variable_shadowing():
    x = 10  # Local variable with the same name
    print("Inside the function, x =", x)

local_variable_shadowing()
print("Global x =", x)
Output:

sql
Copy code
Inside the function, x = 10
Global x = 20
7. Modifying a Global Variable with a Local Variable:
python
Copy code
x = 20  # Global variable

def modify_global_with_local():
    x = 30  # A local variable with the same name
    print("Inside the function, x =", x)

modify_global_with_local()
print("Global x =", x)
Output:

sql
Copy code
Inside the function, x = 30
Global x = 20
8. Global Variable Access Inside a Function:
python
Copy code
global_variable = 50

def access_global_variable():
    print("Inside the function, global_variable =", global_variable)

access_global_variable()
Output:

bash
Copy code
Inside the function, global_variable = 50
9. Global Variable Modification Inside a Function:
python
Copy code
global_variable = 60

def modify_global_variable():
    global global_variable
    global_variable += 10

modify_global_variable()
print("Global variable after modification:", global_variable)
Output:

sql
Copy code
Global variable after modification: 70
10. Using Non-Local with Nested Functions:
python
Copy code
def outer_function():
    outer_variable = 5

    def inner_function():
        nonlocal outer_variable
        outer_variable += 10

    inner_function()
    print("Outer variable (non-local) after modification:", outer_variable)

outer_function()
Output:

sql
Copy code
Outer variable (non-local) after modification: 15
These 10 programs showcase various aspects of local and global variable scopes, no
