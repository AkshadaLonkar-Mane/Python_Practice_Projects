
# BAsic Calculator project:

# 1. Define Functions for operators
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by Zero."
    return x / y


# 2. Define Operators:

def operator():
    operator = input("Enter an operator(+, -, *, /  ): \n")

    if operator in ["+", "-", "*", "/"]:
        num1 = float (input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))

        if operator == "+":
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif operator == "-":
            print(f"{num1} - {num2} = {substract(num1, num2)}")

        elif operator == "*":
            print(f"{num1} * {num2} = {multiple(num1, num2)}")

        elif operator == "/":
            print(f"{num1} / {num2} = {divide (num1, num2)}")
    else:
        print("Invalid Input")


#  3. Calling function:
operator()

# Output:
"""
Enter an operator(+, -, *, /  ): 
*
Enter the 1st number: 12
Enter the 2nd number: 10
12.0 * 10.0 = 120.0
"""