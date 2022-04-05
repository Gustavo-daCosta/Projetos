from os import system

def menu(msg: str):
    tamanhoMsg = len(msg) + 10
    print("=-="*(tamanhoMsg//3+1))
    print(msg.center(tamanhoMsg))
    print("=-="*(tamanhoMsg//3+1))

def showMeasure():
        print('''Select the measure:
[ 1 ] Celsius   (C°)
[ 2 ] Farenheit (F°)
[ 3 ] Kelvin    (K°)''')

def verification(inputText: str):
    while True:
        try:
            var = int(input(inputText))
            if 0 < var < 4:
                break
            else:
                raise ValueError
        except (ValueError, TypeError):
            print("Invalid value! Please type a number between 1 and 3")
    system('cls')
    return var

while True:
    menu("Temperature Converter")
    print('''[ 1 ] Convert temperature
[ 2 ] Temperature measurement formulas
[ 3 ] Exit''')
    option = verification("Select an option: ")

    if option == 1:
        menu("Convert Temperature")
        showMeasure()
        originalMeasure = verification()
        menu("Convert Temperature")
        showMeasure()
        while True:
            try:
                finalMeasure = int(input("Select an option: "))
                if 0 < finalMeasure < 4 and finalMeasure != originalMeasure:
                    break
                elif finalMeasure == originalMeasure:
                    print("Error! The final measure cannot be the same as the original measure.")
                else:
                    raise ValueError
            except (ValueError, TypeError):
                print("Invalid value! Please type a number between 1 and 3")
        
        

    
    elif option == 2:
        print("formulas")

    else:
        print("Goodbye!")
        break