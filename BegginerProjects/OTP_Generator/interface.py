from tkinter import *
from random import randint
from clipboard import copy

app = Tk()
app.title("OTP Generator")
app.iconbitmap("OTP_Generator\images\padlock-logo.ico")
app.configure(background="#344966")
app.geometry("300x200")
app.resizable(False, False)

otp = StringVar()
def generate_otp(digits):
    global lastDigits
    lastDigits = digits
    while True:
        otp_isValid = True
        otp = ''
        for c in range(0, digits):
            otp += str(randint(0, 9))
        for number in range(0, 9):
            counter = otp.count(str(number))
            if counter > 2:
                otp_isValid = False
        if otp_isValid == True:
            break
    copy(otp)
    otpText.forget()
    horizontalPositionOTP = 108
    if digits == 6:
        horizontalPositionOTP = 95
    elif digits == 8:
        horizontalPositionOTP = 75
    otpText.place(x=horizontalPositionOTP, y=62)
    otpText.configure(width=digits)
    otpText.delete('1.0', END)
    otpText.insert(END, otp)

appBackground = "#344966"
textfgColor = "#F0F4EF"

appTitle = Label(app, text="One Time Password", bg=appBackground, fg=textfgColor, font=("Arial", 19, 'bold'))
appTitle.place(x=27, y=5)

otpText = Text(app, width=4, height=1, font=("Arial", 26), bg=appBackground, fg="#B4CDED")
otpText.place(x=108, y=62)

buttonWidth = 8
ButtonFourDigits = Button(app, text="4 Digits", bg=appBackground, fg=textfgColor, width=buttonWidth, command=lambda:generate_otp(4))
ButtonFourDigits.place(x=45, y=130)

ButtonSixDigits = Button(app, text="6 Digits", bg=appBackground, fg=textfgColor, width=buttonWidth, command=lambda:generate_otp(6))
ButtonSixDigits.place(x=115, y=130)

ButtonEightDigits = Button(app, text="8 Digits", bg=appBackground, fg=textfgColor, width=buttonWidth, command=lambda:generate_otp(8))
ButtonEightDigits.place(x=185, y=130)

OBStext = Label(app, text = "OBS: The password is automatically copied to the clipboard.", bg=appBackground, fg=textfgColor, font=("Arial", 8))
OBStext.place(x=2, y=170);

app.mainloop()