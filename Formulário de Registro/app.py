from os import system

while True:
    print(f"{'REGISTRATION FORMULARY':^50}")
    print('''[ 1 ] Register new account
[ 2 ] Login in a existing account
[ 3 ] Exit program''');
    while True:
        try:
            opcao = int(input('Select an option: '));
            if 4 > opcao > 0:
                system('cls')
                break
            else:
                raise ValueError
        except:
            print('ERRO! Tente novamente.')
    if opcao == 1:
        print('teste')