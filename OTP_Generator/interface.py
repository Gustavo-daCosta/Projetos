from tkinter import *
from random import randint
from clipboard import copy

app = Tk()
app.title("OTP GENERATOR")
# app.iconbitmap("images/coin-logo.ico")
app.configure(background="#8a4b1c")
app.geometry("300x200")
app.resizable(False, False)

textfgColor = "white"

appTitle = Label(app, text="OTP GENERATOR", font=("Arial", 20))
appTitle.place(x=0, y=10)


app.mainloop()