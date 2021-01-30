from tkinter import *
import ctypes


def add_number(number):
    cur_value = calc.get()
    if cur_value[0] == '0' and len(cur_value) == 1:
        cur_value = cur_value[1:]
    calc.delete(0, END)
    calc.insert(0, cur_value + number)


def add_operation(operation):
    cur_value = calc.get()
    if cur_value[-1] in '-+/*':
        cur_value = cur_value[:-1]
    calc.delete(0, END)
    calc.insert(0, cur_value + operation)


def calculate():
    cur_value = calc.get()
    if cur_value[-1] in '-+/*':
        cur_value = cur_value + cur_value[:-1]
    calc.delete(0, END)
    calc.insert(0, eval(cur_value))


def make_clear():
    calc.delete(0, END)
    calc.insert(0, '0')


def get_number_button(number):
    return Button(text=number, bd=5, font=('Calibry', 14), command=lambda: add_number(number))


def get_operation_button(operation):
    return Button(text=operation, bd=5, fg='red', font=('Calibry', 14), command=lambda: add_operation(operation))


def calculation_button(operation):
    return Button(text=operation, bd=5, fg='red', font=('Calibry', 14), command=lambda: calculate())


def clear_button(operation):
    return Button(text=operation, bd=5, fg='red', font=('Calibry', 14), command=lambda: make_clear())


SIZE = WIDTH, HEIGHT = (300, 310)

user32 = ctypes.windll.user32
CWIDTH, CHEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

window = Tk()
window.title('Calculator 8.0')
window.geometry(f'{WIDTH}x{HEIGHT}+{int(CWIDTH / 2 - WIDTH / 2)}+{int(CHEIGHT / 2 - HEIGHT / 2)}')
window.resizable(False, False)
window['bg'] = '#b8b9c2'

calc = Entry(window, justify=RIGHT, font=('Calibry', 16), width=18)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

get_number_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
get_number_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
get_number_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
get_number_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
get_number_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
get_number_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
get_number_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
get_number_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
get_number_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
get_number_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

get_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
get_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
get_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
get_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

calculation_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)

clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

window.grid_columnconfigure(0, minsize=75)
window.grid_columnconfigure(1, minsize=75)
window.grid_columnconfigure(2, minsize=75)
window.grid_columnconfigure(3, minsize=75)

window.grid_rowconfigure(1, minsize=70)
window.grid_rowconfigure(2, minsize=70)
window.grid_rowconfigure(3, minsize=70)
window.grid_rowconfigure(4, minsize=70)

window.mainloop()
