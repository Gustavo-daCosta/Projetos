from tkinter import *
from tkinter import messagebox, ttk

app = Tk()
app.title("Conversor de Moedas")
app.geometry( "400x300")
app.resizable(False, False)
app.configure(background="#253a4e")

backgroundColor = '#253a4e'
TextBoxColor = '#2c465b'

Titulo = Label(app, text="Conversor de Moedas", bg=backgroundColor, fg='white', font=("Arial", 20))
Titulo.place(x=60, y=8)

separator = ttk.Separator(app, orient='horizontal')
separator.pack(fill='x', pady=52)

ValorLabel = Label(app, text='Valor :', bg=backgroundColor, fg='white', cnf={"width": 10, "height": 1})
ValorLabel.place(x=2, y=60)

ValorText = Text(app, width=10, height=1)
ValorText.place(x=60, y=60)

app.mainloop()