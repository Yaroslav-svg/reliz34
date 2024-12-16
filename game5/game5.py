import tkinter as tk
import math


import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


def clear():
    entry.delete(0, tk.END)


def percentage():
    try:
        current = entry.get()
        result = eval(current) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


def square_root():
    try:
        current = entry.get()
        result = math.sqrt(float(current))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


root = tk.Tk()
root.title("Калькулятор")


entry = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), 
                  command=lambda value=text: button_click(value)).grid(row=row, column=col)

tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 14), command=clear).grid(row=4, column=3)
tk.Button(root, text="%", padx=18, pady=20, font=('Arial', 14), command=percentage).grid(row=5, column=0)
tk.Button(root, text="√", padx=18, pady=20, font=('Arial', 14), command=square_root).grid(row=5, column=1)

root.mainloop()

