from tkinter import *
from os import system

app = Tk()
app.title("Pomodoro Timer")
app.resizable(False, False)
app.geometry("500x400")

background_image = PhotoImage(file="pomodoro.png")
background_label = Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Timer = Text(app, width=30, height=1, font=("Arial", 20))
Timer.place(x=10, y=10)

app.mainloop()