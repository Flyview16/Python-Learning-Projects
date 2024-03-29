import os

#Calculator
from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multipy(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multipy,
    "/" : divide,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))

    for symbol in operations:
        print(f"{symbol}")

    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")

        num2 = float(input("What is the next number? "))

        function = operations[operation]
        result = function(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            num1 = result
        else:
            should_continue = False
            os.system('cls')
            calculator()


calculator()
