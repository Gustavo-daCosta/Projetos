from tkinter import *
from tkinter.font import BOLD
from game import TicTacToeLines, TicTacToeButtons

app = Tk()
app.title("Tic-Tac-Toe")
app.geometry("400x300")
app.resizable(False, False)
app.configure(background="white")

def startGame():
    # Forget all the widgets in the screen, except the title
    startButton.place_forget()
    exitButton.place_forget()

    TicTacToeLines(app)
    TicTacToeButtons(app)

bgColor = "white"
fgColor = "black"

title = Label(app, text="TIC-TAC-TOE", font=("Arial", 30, BOLD), bg=bgColor, fg=fgColor)
title.place(x=70, y=5)

startButton = Button(app, text="START", font=("Arial", 18), bg="green", width=10, height=1, command=startGame)
startButton.place(x=120, y=120)

exitButton = Button(app, text="EXIT", font=("Arial", 18), bg="red", width=10, height=1)
exitButton.place(x=120, y=190)



app.mainloop()