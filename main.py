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

def calculate(num_list, op_list):
    answer = 0
    for op in op_list:
        if op == "+":
            if op_list.index(op) == 0:
                answer += addition(num_list[0], num_list[1])
                num_list.remove(num_list[0])
                num_list.remove(num_list[0])
        elif op == "-":
            if op_list.index(op) == 0:
                answer += subtraction(num_list[0], num_list[1])
                num_list.remove(num_list[0])
                num_list.remove(num_list[0])
        elif op == "/":
            if op_list.index(op) == 0:
                answer += division(num_list[0], num_list[1])
                num_list.remove(num_list[0])
                num_list.remove(num_list[0])
        elif op == "x":
            if op_list.index(op) == 0:
                answer += multiplication(num_list[0], num_list[1])
                num_list.remove(num_list[0])
                num_list.remove(num_list[0])
    print(answer)

# ----------------------------------------------------------------------------------------------------------------#

display_num = ""

def read_display():
    global display_num
    number_list = []
    operations_list = []
    number = ""
    for char in display_num:
        if char == "/":
            number = float(number)
            number_list.append(number)
            operations_list.append("/")
            number = ""
        elif char == "x":
            number = float(number)
            number_list.append(number)
            operations_list.append("x")
            number = ""
        elif char == "-":
            number = float(number)
            number_list.append(number)
            operations_list.append("-")
            number = ""
        elif char == "+":
            number = float(number)
            number_list.append(number)
            operations_list.append("+")
            number = ""
        else:
            number += char
    number_list.append(float(number))
    print(number_list)
    print(operations_list)
    calculate(number_list, operations_list)

def zero_func():
    global display_num
    display_num += "0"
    canvas.itemconfig(display, text=display_num)


def one_func():
    global display_num
    display_num += "1"
    canvas.itemconfig(display, text=display_num)


def two_func():
    global display_num
    display_num += "2"
    canvas.itemconfig(display, text=display_num)


def three_func():
    global display_num
    display_num += "3"
    canvas.itemconfig(display, text=display_num)


def four_func():
    global display_num
    display_num += "4"
    canvas.itemconfig(display, text=display_num)


def five_func():
    global display_num
    display_num += "5"
    canvas.itemconfig(display, text=display_num)


def six_func():
    global display_num
    display_num += "6"
    canvas.itemconfig(display, text=display_num)


def seven_func():
    global display_num
    display_num += "7"
    canvas.itemconfig(display, text=display_num)


def eight_func():
    global display_num
    display_num += "8"
    canvas.itemconfig(display, text=display_num)


def nine_func():
    global display_num
    display_num += "9"
    canvas.itemconfig(display, text=display_num)


def decimal_func():
    global display_num
    display_num += "."
    canvas.itemconfig(display, text=display_num)
    decimal_button["state"] = "disabled"

def divide_func():
    global display_num
    display_num += "/"
    canvas.itemconfig(display, text=display_num)
    decimal_button["state"] = "normal"

def times_func():
    global display_num
    display_num += "x"
    canvas.itemconfig(display, text=display_num)
    decimal_button["state"] = "normal"

def minus_func():
    global display_num
    display_num += "-"
    canvas.itemconfig(display, text=display_num)
    decimal_button["state"] = "normal"

def plus_func():
    global display_num
    display_num += "+"
    canvas.itemconfig(display, text=display_num)
    decimal_button["state"] = "normal"

def clear_display():
    global display_num
    display_num = ""
    canvas.itemconfig(display, text=display_num)

window = Tk()
window.title("Calculator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=100)
display = canvas.create_text(
    100, 50, text=display_num, justify="center", width=200, font=("San Fransisco", 20))
canvas.grid(row=0, column=0, columnspan=4)

seven_button = Button(text=7, font=("San Fransisco", 20),
                      relief="groove", width=3, height=1, command=seven_func)
seven_button.grid(row=1, column=0)

eight_button = Button(text=8, font=("San Fransisco", 20),
                      relief="groove", width=3, height=1, command=eight_func)
eight_button.grid(row=1, column=1)

nine_button = Button(text=9, font=("San Fransisco", 20),
                     relief="groove", width=3, height=1, command=nine_func)
nine_button.grid(row=1, column=2)

divide_button = Button(text="/", font=("San Fransisco", 20),
                       relief="groove", width=3, height=1, command=divide_func)
divide_button.grid(row=1, column=3)

four_button = Button(text=4, font=("San Fransisco", 20),
                     relief="groove", width=3, height=1, command=four_func)
four_button.grid(row=2, column=0)

five_button = Button(text=5, font=("San Fransisco", 20),
                     relief="groove", width=3, height=1, command=five_func)
five_button.grid(row=2, column=1)

six_button = Button(text=6, font=("San Fransisco", 20),
                    relief="groove", width=3, height=1, command=six_func)
six_button.grid(row=2, column=2)

times_button = Button(text="x", font=("San Fransisco", 20),
                      relief="groove", width=3, height=1, command=times_func)
times_button.grid(row=2, column=3)

one_button = Button(text=1, font=("San Fransisco", 20),
                    relief="groove", width=3, height=1, command=one_func)
one_button.grid(row=3, column=0)

two_button = Button(text=2, font=("San Fransisco", 20),
                    relief="groove", width=3, height=1, command=two_func)
two_button.grid(row=3, column=1)

three_button = Button(text=3, font=("San Fransisco", 20),
                      relief="groove", width=3, height=1, command=three_func)
three_button.grid(row=3, column=2)

minus_button = Button(text="-", font=("San Fransisco", 20),
                      relief="groove", width=3, height=1, command=minus_func)
minus_button.grid(row=3, column=3)

zero_button = Button(text=0, font=("San Fransisco", 20),
                     relief="groove", width=3, height=1, command=zero_func)
zero_button.grid(row=4, column=0)

decimal_button = Button(text=".", font=("San Fransisco", 20),
                        relief="groove", width=3, height=1, command=decimal_func)
decimal_button.grid(row=4, column=1)

equals_button = Button(text="=", font=("San Fransisco", 20),
                       relief="groove", width=3, height=1, command=read_display)
equals_button.grid(row=4, column=2)

plus_button = Button(text="+", font=("San Fransisco", 20),
                     relief="groove", width=3, height=1, command=plus_func)
plus_button.grid(row=4, column=3)

plus_button = Button(text="Reset", font=("San Fransisco", 20),
                     relief="groove", command=clear_display)
plus_button.grid(row=5, column=0, columnspan=4)

window.mainloop()
