def addition(num1, num2):
    pass


def subtraction(num1, num2):
    pass


def multiplication(num1, num2):
    pass


def division(num1, num2):
    pass


num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")
operation = input("Enter an operation (+,-,x,/): ")

if operation == "+":
    print(addition(num1, num2))
elif operation == "-":
    print(subtraction(num1, num2))
elif operation == "x":
    print(multiplication(num1, num2))
elif operation == "/":
    print(division(num1, num2))
else:
    print("Invalid input")
