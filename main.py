def addition(num1, num2):
    result = num1 + num2
    return result


def subtraction(num1, num2):
    result = num1 - num2
    return result


def multiplication(num1, num2):
    result = num1 * num2
    return result


def division(num1, num2):
    result = num1 / num2
    return result


def check_if_num(input):
    try:
        num = float(input)
        return True
    except ValueError:
        return False


num1 = input("Enter a number: ")
while not check_if_num(num1):
    print("Invalid input")
    num1 = input("Enter a number: ")
num1 = float(num1)
num2 = input("Enter a second number: ")
while not check_if_num(num2):
    print("Invalid input")
    num2 = input("Enter a second number: ")
num2 = float(num2)
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
    print("Invalid operation")
