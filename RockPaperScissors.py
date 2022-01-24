# Rock paper scissors game gui game written in python with tkinter by kiisuhh#2750

import tkinter as tk
from random import randrange

enemy = ""

def action(pick):
    global enemy
    random = randrange(3)
    if random == 1:
        enemy = "ROCK"
    elif random == 2:
        enemy = "PAPER"
    else:
        enemy = "SCISSORS"

    print("------------------")
    print("User Took: " + pick)
    print("Computer Took " + enemy)


root = tk.Tk()
root.geometry("400x200")
root.title("Rock Paper Scissors")

WinOrLose = tk.Label(text="Waiting for an action")
WinOrLose.grid(row=1, column=5)

ComputerAction = tk.Label(text="Placeholder")
ComputerAction.grid(row=2, column=5)

btn_rock = tk.Button(text="Rock", command=lambda: action("ROCK"))
btn_rock.grid(row=3, column=3, columnspan=3, sticky = tk.W+tk.E)
btn_paper = tk.Button(text="Paper", command=lambda: action("PAPER"))
btn_paper.grid(row=4, column=3, columnspan=3, sticky = tk.W+tk.E)
btn_scissors = tk.Button(text="Scissors", command=lambda: action("SCISSORS"))
btn_scissors.grid(row=5, column=3, columnspan=3, sticky = tk.W+tk.E)

root.mainloop()
