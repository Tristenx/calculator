from tkinter import *


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


window = Tk()
window.title("Calculator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=100)
display = canvas.create_text(
    100, 50, text="this is a display", justify="center", width=200, font=("San Fransisco", 20))
canvas.grid(row=0, column=0, columnspan=4)

seven_button = Button(text=7, font=("San Fransisco", 20),
                      relief="groove", width=3, height=1)
seven_button.grid(row=1, column=0)

eight_button = Button(text=8, font=("San Fransisco", 20),
                      relief="groove", width=3, height=1)
eight_button.grid(row=1, column=1)

nine_button = Button(text=9, font=("San Fransisco", 20),
                     relief="groove", width=3, height=1)
nine_button.grid(row=1, column=2)

divide_button = Button(text="÷", font=("San Fransisco", 20),
                       relief="groove", width=3, height=1)
divide_button.grid(row=1, column=3)

four_button = Button(text=4, font=("San Fransisco", 20),
                     relief="groove", width=3, height=1)
four_button.grid(row=2, column=0)

five_button = Button(text=5, font=("San Fransisco", 20),
                     relief="groove", width=3, height=1)
five_button.grid(row=2, column=1)

six_button = Button(text=6, font=("San Fransisco", 20),
                    relief="groove", width=3, height=1)
six_button.grid(row=2, column=2)

times_button = Button(text="x", font=("San Fransisco", 20),
                      relief="groove", width=3, height=1)
times_button.grid(row=2, column=3)

one_button = Button(text=1, font=("San Fransisco", 20),
                    relief="groove", width=3, height=1)
one_button.grid(row=3, column=0)

two_button = Button(text=2, font=("San Fransisco", 20),
                    relief="groove", width=3, height=1)
two_button.grid(row=3, column=1)

three_button = Button(text=3, font=("San Fransisco", 20),
                      relief="groove", width=3, height=1)
three_button.grid(row=3, column=2)

minus_button = Button(text="-", font=("San Fransisco", 20),
                      relief="groove", width=3, height=1)
minus_button.grid(row=3, column=3)

zero_button = Button(text=0, font=("San Fransisco", 20),
                     relief="groove", width=3, height=1)
zero_button.grid(row=4, column=0)

decimal_button = Button(text=".", font=("San Fransisco", 20),
                        relief="groove", width=3, height=1)
decimal_button.grid(row=4, column=1)

equals_button = Button(text="=", font=("San Fransisco", 20),
                       relief="groove", width=3, height=1)
equals_button.grid(row=4, column=2)

plus_button = Button(text="+", font=("San Fransisco", 20),
                     relief="groove", width=3, height=1)
plus_button.grid(row=4, column=3)

window.mainloop()
