from os import system

def Menu(msg):
    msgLength = len(msg) + 10
    print("="*msgLength)
    print(msg.center(msgLength))
    print("="*msgLength)

while True:
    Menu("Formulário de Registro")
    print('''[ 1 ] Registrar uma nova conta
[ 2 ] Entrar em uma conta existente
[ 3 ] Sair''')
    while True:
        try:
            opcao = int(input("Selecione uma opção: "))
            if 0 < opcao < 4:
                break
            else:
                raise ValueError
        except (ValueError, TypeError):
            print("ERRO! Valor inválido, tente novamente.")
    
    if opcao == 1:
        teste = open("teste.txt", "a")
        print(teste)