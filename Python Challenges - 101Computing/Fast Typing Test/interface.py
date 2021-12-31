from tkinter import *
import time
from os import system
from random import randint

app = Tk()
app.title("Fast Typing Test")
app.geometry("600x550")

def semComando():
    print("Sem comando")

barra_menu = Menu(app)

menuHelp = Menu(barra_menu, tearoff=0)
menuHelp.add_command(label="How the app works?", command=semComando)
menuHelp.add_command(label="Pangram's list")
barra_menu.add_cascade(label="Help", menu=menuHelp)

menuAbout = Menu(barra_menu, tearoff=0)
menuAbout.add_command(label="Source Code", command=semComando)
menuAbout.add_command(label="Credits", command=semComando)
menuAbout.add_command(label="About", command=semComando)

app.config(menu=barra_menu)

titulo = Label(app, text="Fast Typing Test Challenge", font=("Helvetica", 20))
titulo.pack()

textoMenu = '''Level [1] - Type the Alphabet
Level [2] - Type the following quote: "The quick brown fox jumps over the lazy dog"
Level [3] - Type a random pangram of the list
— “The quick brown fox jumps over the lazy dog”
— “The five boxing wizards jump quickly”
— “Pack my box with five dozen liquor jugs”
— "The jay, pig, fox, zebra and my wolves quack!"
— "By Jove, my quick study of lexicography won a prize!"'''

Menu = Label(app, text=textoMenu, font=("Helvetica", 12))
Menu.place(x=10, y=40)

app.mainloop()