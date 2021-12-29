from random import randint

while True:
    dado1 = dado2 = 0
    tentJogador1 = tentJogador2 = 0
    print('                 JOGO DE DADOS')
    while True:
        try:
            jogador1 = str(input('Digite o nome do primeiro jogador: '))
            jogador2 = str(input('Digite o nome do segundo jogador: '))
            break
        except:
            print('ERRO! Tente novamente')
    while True:
        if dado1 != 6:
            dado1 = randint(1, 6)
            tentJogador1 += 1
        if dado2 != 6:
            dado2 = randint(1, 6)
            tentJogador2 += 1
        if dado1 == 6 and dado2 == 6:
            break
    print('-'*50)
    print(f'Quantidade de tentativas de {jogador1}: {tentJogador1}')
    print(f'Quantidade de tentativas de {jogador2}: {tentJogador2}')
    print('-'*50)
    if tentJogador1 < tentJogador2:
        print(f'Parábens {jogador1}! Você venceu.')
    elif tentJogador1 > tentJogador2:
        print(f'Parábens {jogador2}! Você venceu.')
    else:
        print('UAU! Houve um empate.')