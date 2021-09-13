from random import randint

erros = acertos = 0

def inp_ut(msg, incremento):
    while True:
        resp = int(input(msg))
        if resp == incremento:
            print('Parábens! Você acertou.')
        else:
            print('Infelizmente você errou.')

while True:
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    soma = n1 + n2
    
    # MENU
    print(' JOGO DE SOMA '.center(50, '-'))
    print('''[ 1 ] Soma comum
[ 2 ] Soma com valor faltante
[ 3 ] Conjunto de somas
[ 4 ] Sair do jogo.''')
    print('-'*50)
    while True:
        opcao = int(input('Escolha uma opção: '))
        print(opcao)
        if (opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4):
            break
        else:
            print('Erro! A opção digitada é inválida, tente novamente.')

    if opcao == 1:
    # Soma comum
        print('SOMA COMUM'.center(50, '-'))
        print(f'{n1} + {n2} = ?')
        print('-'*50)
        inp_ut('Digite o resultado da soma: ', soma)

    elif opcao == 2:
    # Soma com um dos valores faltando
        print(' SOMA COM VALOR FALTANTE '.center(50, '-'))
        print(f'{n1} + ? = {soma}')
        print('-'*50)
        inp_ut('Digite o valor faltante: ', n2)

    elif opcao == 3:
    # Conjunto de somas
        while True:
            try:
                quant = int(input('Digite a quantidade de somas (entre 1 e 20): '))
            except:
                print('Erro! Digite um valor inteiro de 1 a 20.')
            if (isinstance(quant, int) is True) and (quant >= 1 and quant <= 20):
                print(f'Serão geradas {quant} somas...')
                break
        for c in range(0, quant):
            n1 = randint(1, 100)
            n2 = randint(1, 100)
            soma = n1+ n2
            print(f' SOMA N°{c+1} '.center(50, '-'))
            print(f'Soma {c+1}:  {n1} + {n2} = ?')
            resposta = int(input('Digite o resultado: '))
            if resposta == soma:
                print('Parábens! Você acertou!')
                acertos += 1
            else:
                print(f'Infelizmente você errou. O resultado da soma é {soma}')
                erros += 1

    elif opcao == 4:
        print('Finalizando...')
        break

    else:
        print('Erro! A opção digitada é inválida, tente novamente.')