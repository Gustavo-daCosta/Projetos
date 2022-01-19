from os import system #, replace
from PIL import Image
import qrcode
import validators

def Menu(msg):
    tamanhomsg = len(msg) + 4
    print('-' * tamanhomsg)
    print(msg.center(tamanhomsg))
    print('-' * tamanhomsg)

c = 0
while True:
    Menu('QR CODE GENERATOR')
    print('''[ 1 ] USE A LINK
[ 2 ] USE SOME TEXT
[ 3 ] USE A WHATSAPP PHONE NUMBER
[ 4 ] CHECK PRE-DEFINED OPTIONS
[ 5 ] SELECT FILE TYPE
[ 6 ] EXIT''')
    while True:
        try:
            option = int(input('Select an option: '))
        except ValueError:
            print('ERROR! Try again.')
        finally:
            if 0 < option <= 6:
                system('cls')
                break
            else:
                print('ERROR! Invalid option, try again!')
    if option == 1:
        Menu('QR CODE => LINK')
        print("OBS: Don't forget the 'http:\\' or 'https:\\' in the URL.")
        while True:
            link = str(input('Paste the link here: '))
            if validators.url(link) is True:
                img = qrcode.make(link)
                if c == 0:
                    img.save("QRcodeLINK.jpg")
                else:
                    img.save(f"QRcodeLINK({c}).jpg")
                c += 1
                break
            else:
                print('Invalid link! Try again.')
                input('Press ENTER to continue...')
                system('cls')
    elif option == 2:
        Menu('QR CODE => TEXT')

    elif option == 3:
        Menu('QR CODE => WHATSAPP PHONE NUMBER')
        print("OBS: Type only numbers and don't forget about the country code!")
        while True:
            try:
                phoneNumber = int(input('Type or paste the phone number: '))
            except ValueError:
                print('ERROR! Invalid phone number, please try again.')
            finally:
                if 9 < phoneNumber <= 13:
                    img = qrcode.make(f"wa.me\+{phoneNumber}")

    elif option == 4:
        Menu("PRE-DEFINED OPTIONS")