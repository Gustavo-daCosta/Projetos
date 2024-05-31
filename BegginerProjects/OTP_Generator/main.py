# OTP = One Time Password

from random import randint
from clipboard import copy
from os import system

def menu(msg):
    system('cls')
    msgLength = len(msg) + 10
    print("=" * msgLength)
    print(msg.center(msgLength))
    print("=" * msgLength)

def generate_otp(digits):
    global otp
    while True:
        otp_isValid = True
        otp = ''
        for c in range(0, digits):
            otp += str(randint(0, 9))
        for number in range(0, 9):
            counter = otp.count(str(number))
            if counter >= (digits / 2):
                otp_isValid = False
        if otp_isValid == True:
            break
    menu(f"{digits}-DIGIT OTP")
    print(f"OTP: {otp}\n")
    copy(otp)
    print('The password has been copied to the clipboard.')
    input('press ENTER to continue...')

while True:
    menu("ONE TIME PASSWORD")
    print('''[ 1 ] 4-DIGIT ONE TIME PASSWORD
[ 2 ] 6-DIGIT ONE TIME PASSWORD
[ 3 ] 8-DIGIT ONE TIME PASSWORD
[ 4 ] EXIT PROGRAM''')
    while True:
        try:
            option = int(input('Select an option: '))
        except:
            print('ERROR! Try again.')
        finally:
            if 0 < option <= 4:
                system('cls')
                break
            else:
                print('ERROR! Invalid option, try again.')
    if option == 1:
        generate_otp(4)
    elif option == 2:
        generate_otp(6)
    elif option == 3:
        generate_otp(8)

    else:
        menu("EXIT PROGRAM")
        input("Press ENTER to exit the program...")
        print('Goodbye!')
        break