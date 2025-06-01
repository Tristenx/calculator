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


def get_new_num():
    new_num = input("Enter a number: ")
    while not check_if_number(new_num):
        print("Invalid input")
        new_num = input("Enter a number: ")
    new_num = float(new_num)
    return new_num


current_num = get_new_num()

calc_on = True
while calc_on:
    operation = input("Enter an operation (+,-,x,/,=): ")
    if operation == "=":
        calc_on = False
    elif operation == "+":
        current_num = addition(current_num, get_new_num())
    elif operation == "-":
        current_num = subtraction(current_num, get_new_num())
    elif operation == "x":
        current_num = multiplication(current_num, get_new_num())
    elif operation == "/":
        current_num = division(current_num, get_new_num())
    else:
        print("Invalid operation")

print(current_num)
