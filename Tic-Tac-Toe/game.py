from tkinter import *
from tkinter.font import BOLD
from turtle import bgcolor, color

bgColor = "white"
fgColor = "black"

def TicTacToeButtons(app):
    app.geometry("400x450")
    borderVar = 1
    '''
    A1 | A2 | A3
    ---+----+---
    B1 | B2 | B3
    ---+----+---
    C1 | C2 | C3
    '''
    # -> A1 | A2 | A3
    A1Button = Button(app, text=" ", width=13, height=5, bg=bgColor, fg=fgColor, borderwidth=borderVar)
    A1Button.place(x=50, y=75)

    A2Button = Button(app, text=" ", width=13, height=5, bg=bgColor, fg=fgColor, borderwidth=borderVar)
    A2Button.place(x=159, y=75)

    A3Button = Button(app, text=" ", width=13, height=5, bg=bgColor, fg=fgColor, borderwidth=borderVar)
    A3Button.place(x=267, y=75)

    # -> B1 | B2 | B3
    B1Button = Button(app, text=" ", width=13, height=5, bg=bgColor, fg=fgColor, borderwidth=borderVar)
    B1Button.place(x=50, y=167)

    B2Button = Button(app, text=" ", width=13, height=5, bg=bgColor, fg=fgColor, borderwidth=borderVar)
    B2Button.place(x=159, y=167)

    B3Button = Button(app, text=" ", width=13, height=5, bg=bgColor, fg=fgColor, borderwidth=borderVar)
    B3Button.place(x=267, y=167)

    # -> C1 | C2 | C3
    C1Button = Button(app, text=" ", width=13, height=5, bg=bgColor, fg=fgColor, borderwidth=borderVar)
    C1Button.place(x=50, y=260)

    C2Button = Button(app, text=" ", width=13, height=5, bg=bgColor, fg=fgColor, borderwidth=borderVar)
    C2Button.place(x=159, y=260)

    C3Button = Button(app, text=" ", width=13, height=5, bg=bgColor, fg=fgColor, borderwidth=borderVar)
    C3Button.place(x=267, y=260)


def TicTacToeLines(app):
    global firstHorizontalLine, secondHorizontalLine, firstVerticalLine, secondVerticalLine

    firstHorizontalLine = Canvas(app, width=310, height=2, bg="black", borderwidth=0, border=0)
    firstHorizontalLine.place(x=50, y=160)

    secondHorizontalLine = Canvas(app, width=310, height=2, bg="black", borderwidth=0, border=0)
    secondHorizontalLine.place(x=50, y=252)

    firstVerticalLine = Canvas(app, width=2, height=280, bg="black", borderwidth=0, border=0)
    firstVerticalLine.place(x=150, y=70)

    secondVerticalLine = Canvas(app, width=2, height=280, bg="black", borderwidth=0, border=0)
    secondVerticalLine.place(x=260, y=70)

def returnToMenu():
    firstHorizontalLine.place_forget()
    secondHorizontalLine.place_forget()
    firstVerticalLine.place_forget()
    secondVerticalLine.place_forget()

def adjacentButtons(app):
    returnButton = Button(app, text="<", font=("Arial", 50), borderwidth=0, bg="black", command=)
    returnButton.place(x=0, y=0)
