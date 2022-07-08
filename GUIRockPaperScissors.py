# Rock paper scissors  gui game written in python with tkinter by kiisuhh#2750

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
    if pick == "ROCK":
        if enemy == "ROCK":
            draw(pick)
        elif enemy == "PAPER":
            lost(pick)
        else:
            won(pick)
    elif pick == "PAPER":
        if enemy == "ROCK":
            won(pick)
        elif enemy == "PAPER":
            draw(pick)
        else:
            lost(pick)
    else:
        if enemy == "ROCK":
            lost(pick)
        elif enemy == "PAPER":
            won(pick)
        else:
            draw(pick)


def won(pick):
    print("User won")
    WinOrLose.configure(text="You Won!")
    ComputerAction.configure(text="You took " + str(pick) + " | Computer Took: " + str(enemy))
    btn_rock.grid_forget()
    btn_paper.grid_forget()
    btn_scissors.grid_forget()
    btn_pa.grid(row=4, column=3, columnspan=6, sticky ="EW")
    btn_quit.grid(row=5, column=3, columnspan=6, sticky="EW")

def lost(pick):
    print("User lost")
    WinOrLose.configure(text="You Lost!")
    ComputerAction.configure(text="You took " + str(pick) + " | Computer Took: " + str(enemy))
    btn_rock.grid_forget()
    btn_paper.grid_forget()
    btn_scissors.grid_forget()
    btn_pa.grid(row=4, column=3, columnspan=6, sticky="EW")
    btn_quit.grid(row=5, column=3, columnspan=6, sticky="EW")

def draw(pick):
    print("Draw Round")
    WinOrLose.configure(text="Draw!")
    ComputerAction.configure(text="You took " + str(pick) + " | Computer Took: " + str(enemy))
    btn_rock.grid_forget()
    btn_paper.grid_forget()
    btn_scissors.grid_forget()
    btn_pa.grid(row=4, column=3, columnspan=6, sticky="EW")
    btn_quit.grid(row=5, column=3, columnspan=6, sticky="EW")


def playagain():
    WinOrLose.configure(text="Waiting for an action...")
    ComputerAction.configure(text="---------------------------------------------")
    btn_pa.grid_forget()
    btn_quit.grid_forget()
    btn_rock.grid(row=3, column=3, columnspan=6, sticky="EW")
    btn_paper.grid(row=4, column=3, columnspan=6, sticky="EW")
    btn_scissors.grid(row=5, column=3, columnspan=6, sticky="EW")


root = tk.Tk()
root.geometry("250x125")
root.title("Rock Paper Scissors")
root.resizable(height=False, width=False)

WinOrLose = tk.Label(text="Waiting for an action...", width=20, height=1)
WinOrLose.grid(row=1, column=5, sticky="EW")

ComputerAction = tk.Label(text="---------------------------------------------")
ComputerAction.grid(row=2, column=5)

btn_rock = tk.Button(text="Rock", width=5, command=lambda: action("ROCK"))
btn_rock.grid(row=3, column=3, columnspan=6, sticky="EW")
btn_paper = tk.Button(text="Paper", command=lambda: action("PAPER"))
btn_paper.grid(row=4, column=3, columnspan=6, sticky="EW")
btn_scissors = tk.Button(text="Scissors", command=lambda: action("SCISSORS"))
btn_scissors.grid(row=5, column=3, columnspan=6, sticky="EW")

btn_pa = tk.Button(text="Play Again!", command=playagain)
btn_quit = tk.Button(text="QUIT", command=lambda: root.destroy())


root.mainloop()
