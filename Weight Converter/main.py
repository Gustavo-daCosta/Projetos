'''
Kilogram 
Hectogram 
Dekagram 
Gram 
Dekagram 
Centigram 
Milligram
'''
from os import system

def Menu(msg):
    msgHeigth = len(msg) + 10
    system('cls')
    print('='*msgHeigth)
    print(msg.center(msgHeigth))
    print('='*msgHeigth)

def optionsMenu(*optionsList):
    for option in optionsList:
        print(f"[ {(optionsList.index(option) + 1)} ] {option}")

while True:
    Menu("WEIGHT CONVERTER")
    optionsMenu("Convert weight", "Exit program")

    while True:
        try:
            option = int(input('Select an option: '))
            if option != 1 and option != 2:
                raise ValueError
            else:
                break
        except (ValueError, TypeError):
            print("ERROR! Please type the number 1 or 2.")
    if option == 1:
        Menu("WEIGHT CONVERTER")
        print("select source weight measurement: ")
        optionsMenu("Kilogram (kg)", "Hectogram (hg)", "Dekagram (dag)", "Gram (g)", "Dekagram (dg)", "Centigram (cg)", "Milligram (mg)")

        

    
    elif option == 2:
        print("Goodbye!")
        break