from tkinter import *
from tkinter.font import BOLD

app = Tk()
app.title("Counter")
app.geometry("250x130")
app.configure(background="white")
app.resizable(False, False)

def counter():
    actualNumber = int(showCounter.get(1.0, "end-1c"))
    newNumber = actualNumber + 1
    horizontalPosition = 113
    numberLength = len(str(newNumber))
    if numberLength > 1:
        horizontalPosition -= 8 * (numberLength - 1)
    showCounter.place(x=horizontalPosition, y=30)
    showCounter.configure(state=NORMAL, width=numberLength)
    showCounter.delete('1.0', END)
    showCounter.insert(END, str(newNumber))
    showCounter.configure(state=DISABLED)

def restart():
    showCounter.place(x=113, y=30)
    showCounter.configure(state=NORMAL, width=1)
    text = "0"
    showCounter.delete('1.0', END)
    showCounter.insert(END, text)
    showCounter.configure(state=DISABLED)


title = Label(app, text="You clicked the button this many times:", font=("Arial", 10), bg="white", fg="black")
title.place(x=7, y=1)

showCounter = Text(font=("Arial", 26, BOLD), borderwidth=0, bg="white", fg="black", height=1, width=1)
showCounter.insert(END, "0")
showCounter.place(x=113, y=30)

picture = PhotoImage(file="Counter App/images/plus-symbol-button (Personalizado).png")

counterButton = Button(app, image=picture, width=35, height=35, borderwidth=0, bg="white", command=counter)
counterButton.place(x=108, y=85)

restartButton = Button(app, text="Restart", bg="#c4e0f2", fg="black", font=("Arial", 11), width=6, height=1, command=restart)
restartButton.place(x=15, y=90)

exitButton = Button(app, text="Exit", bg="red", fg="white", font=("Arial", 11), width=4, height=1, command = app.destroy)
exitButton.place(x=175, y=90)

app.mainloop()

# text.configure(state=DISABLED)