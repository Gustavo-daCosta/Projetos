from tkinter import *
import db_commands

app = Tk()
app.title("Library Management System")
app.geometry("700x450")
app.resizable(False, False)


bgIMG = PhotoImage(file = "images/clip-library-1.png")
limg = Label(app, i = bgIMG)
limg.pack()

TitleText = Label(app,
    text = "  Library Management System  ",
    font = ("Arial", 28),
    borderwidth = 3,
    relief = "ridge"
)
TitleText.place(x=100, y=8)

ButtonAddBook = Button(app, text="Add Book Details", bg="black", fg="white", font=("Arial", 16))
ButtonAddBook.place(x=200, y=150)


app.mainloop()