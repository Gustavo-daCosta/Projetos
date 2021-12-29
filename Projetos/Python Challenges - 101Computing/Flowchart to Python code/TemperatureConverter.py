from os import system

while True:
    print('''       Temperature Converter
    
    [ 1 ] Celsius to Fahrenheit
    [ 2 ] Fahrenheit to Celsius
    [ 3 ] Exit''')
    while True:
        try:
            option = int(input('Select one option: '))
            if isinstance(option, int) and 0 < option < 4:
                system(command='cls')
                break
        except ValueError:
            print('ERROR! Try again.')
    if option == 1:
        while True:
            try:
                celsius = float(input('Celsius: '))
                break
            except ValueError:
                print('ERROR! Try again.')
                input('Type ENTER to continue...')
                system(command='cls')
        fahrenheit = celsius * 1.8 + 32
        print('=-='*15)
        print(f'{celsius}° Celsius in Fahrenheit: F°{fahrenheit}')
    elif option == 2:
        while True:
            try:
                fahrenheit = float(input('Fahrenheit: '))
                break
            except ValueError:
                print('ERROR! Try again.')
                input('Type ENTER to continue...')
                system(command='cls')
        celsius = (fahrenheit - 32) / 1.8
        print('=-='*15)
        print(f'{fahrenheit}° Fahrenheit in Celsius: C°{celsius}')
    elif option == 3:
        print('Goodbye!')
        exit()