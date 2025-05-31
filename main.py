def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def check_if_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False


def perform_operation(user_input, num1, num2):
    if user_input == "+":
        print(addition(num1, num2))
    elif user_input == "-":
        print(subtraction(num1, num2))
    elif user_input == "x":
        print(multiplication(num1, num2))
    elif user_input == "/":
        print(division(num1, num2))
    else:
        print("Invalid operation")


num1 = input("Enter a number: ")
while not check_if_number(num1):
    print("Invalid input")
    num1 = input("Enter a number: ")
num1 = float(num1)

operation = input("Enter an operation (+,-,x,/): ")

num2 = input("Enter a second number: ")
while not check_if_number(num2):
    print("Invalid input")
    num2 = input("Enter a second number: ")
num2 = float(num2)

perform_operation(operation, num1, num2)
