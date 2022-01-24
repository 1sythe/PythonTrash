# tkinter gui calculator written in python by kiisuhh#2750
import tkinter as tk


calc = ""


def add(symbol):
    global calc
    calc += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, calc)


def calculate():
    global calc
    try:
        calc = str(eval(calc))
        result.delete(1.0, "end")
        result.insert(1.0, calc)
    except:
        clear()
        result.insert(1.0, "Error")


def clear():
    global calc
    calc = ""
    result.delete(1.0, "end")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")
root.resizable(height=False, width=False)

result = tk.Text(root, height=1, width=16, font=("Arial", 24))
result.grid(columnspan=5)

num1 = tk.Button(root, text="1", width=5, font=("Arial", 10), command=lambda: add(1))
num1.grid(row=2, column=1)
num2 = tk.Button(root, text="2", width=5, font=("Arial", 10), command=lambda: add(2))
num2.grid(row=2, column=2)
num3 = tk.Button(root, text="3", width=5, font=("Arial", 10), command=lambda: add(3))
num3.grid(row=2, column=3)
num4 = tk.Button(root, text="4", width=5, font=("Arial", 10), command=lambda: add(4))
num4.grid(row=3, column=1)
num5 = tk.Button(root, text="5", width=5, font=("Arial", 10), command=lambda: add(5))
num5.grid(row=3, column=2)
num6 = tk.Button(root, text="6", width=5, font=("Arial", 10), command=lambda: add(6))
num6.grid(row=3, column=3)
num7 = tk.Button(root, text="7", width=5, font=("Arial", 10), command=lambda: add(7))
num7.grid(row=4, column=1)
num8 = tk.Button(root, text="8", width=5, font=("Arial", 10), command=lambda: add(8))
num8.grid(row=4, column=2)
num9 = tk.Button(root, text="9", width=5, font=("Arial", 10), command=lambda: add(9))
num9.grid(row=4, column=3)
num0 = tk.Button(root, text="0", width=5, font=("Arial", 10), command=lambda: add(0))
num0.grid(row=5, column=3)

button_plus = tk.Button(root, text="+", width=5, font=("Arial", 10), command=lambda: add("+"))
button_plus.grid(row=2, column=4)
button_minus = tk.Button(root, text="-", width=5, font=("Arial", 10), command=lambda: add("-"))
button_minus.grid(row=3, column=4)
button_multiply = tk.Button(root, text="*", width=5, font=("Arial", 10), command=lambda: add("*"))
button_multiply.grid(row=4, column=4)
button_divide = tk.Button(root, text="/", width=5, font=("Arial", 10), command=lambda: add("/"))
button_divide.grid(row=5, column=4)

ClipFrame = tk.Frame(root)
button_right = tk.Button(ClipFrame, text=")", width=2, font=("Arial", 10), command=lambda: add(")"))
button_right.grid(row=6, column=4)
button_left = tk.Button(ClipFrame, text="(", width=2, font=("Arial", 10), command=lambda: add("("))
ClipFrame.grid(row=6, column=4)
button_right.pack(side="right")
button_left.pack(side="left")

button_clear = tk.Button(root, text="Clear", width=5, font=("Arial", 10), command=clear)
button_clear.grid(row=5, column=1, columnspan=2, sticky=tk.W+tk.E)
button_equals = tk.Button(root, text="=", width=1, font=("Arial", 10), command=calculate)
button_equals.grid(row=6, column=1, columnspan=3, sticky=tk.W+tk.E)


root.mainloop()
