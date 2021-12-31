# INCOMPLETO
# Programa ainda não funciona e to com preguiça demais para arrumar

from os import system

while True:
    system(command='cls')
    print('''         Original Price Calculator
[ 1 ] Calculate Original Price
[ 2 ] Calculate Discount
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
                discountedPrice = float(input('Discounted Price: '))
                discount = int(input('Percentage discount? ex: Type 20 for 20%  '))
                break
            except ValueError:
                print('ERROR! Try again.')
                input('Type ENTER to continue...')
                system(command='cls')
        originalPrice = discountedPrice/(1 - discount/100)
        print('=-='*15)
        print(f'Original Price: {originalPrice}')
    elif option == 2:
        while True:
            try:
                totalPrice = float(input('Total Price? '))
                percentageDiscount = int(input('Percentage discount? ex: Type 20 for 20%  '))
            except ValueError:
                print('ERROR! Try again.')
                input('Type ENTER to continue...')
                system(command='cls')
            discountedPrice = totalPrice - totalPrice*(percentageDiscount/100)
            print('=-='*15)
            print(f'Discounted Price: {discountedPrice}')
    elif option == 3:
        print('Goodbye!')
        exit()