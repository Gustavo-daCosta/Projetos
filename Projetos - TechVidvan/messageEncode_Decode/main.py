from base64 import b64encode, b64decode
from os import system
from clipboard import copy

# Por enquanto só tenho que arranjar uma maneira de ele colocar as mensagens nos arquivos de texto
# ESSA MERDA NAO FUNCIONA VOU ARRUMAR UM DIA SE EU CRIAR CORAGEM

def Menu(msg):
    global tamanhoMsg
    tamanhoMsg = len(msg) + 12
    print('-' * tamanhoMsg)
    print(msg.center(tamanhoMsg))
    print('-' * tamanhoMsg)

def codificar_mensagem(msgDescodificada):
    system('cls')
    Menu('Codificar Mensagem')
    msgCodificada = b64encode(bytes(msgDescodificada, 'utf-8')).strip()
    copy(str(msgCodificada))
    print('A mensagem foi codificada com sucesso e copiada para a sua área de transferência.')
    return msgCodificada

def descodificar_mensagem(msgCodificada):
    system('cls')
    Menu('Descodificar Mensagem')
    msgDescodificada = b64decode(msgCodificada.strip()).decode('utf-8')
    copy(msgDescodificada)
    print('A mensagem foi descodificada com sucesso e copiada para a sua área de transferência.')
    return msgDescodificada

while True:
    system('cls')
    while True:
        Menu('Codificador de mensagens')
        print('''[ 1 ] Codificar mensagem
[ 2 ] Decodificar mensagem
[ 3 ] Sair''')
        try:
            opcao = int(input('Selecione uma opção: '))
        except ValueError:
            print('ERRO! Valor inválido, tente novamente.')
        except KeyboardInterrupt:
            exit()
        finally:
            if 0 < opcao < 4:
                system('cls')
                break
            else:
                print('Opção inválida! Digite um valor entre 1 e 3.')
                input('Aperte ENTER para continuar...')
                system('cls')
    if opcao == 1:
        Menu('Codificar Mensagem')
        while True:
            msgDescodificada = str(input('Digite ou copie a mensagem: ')).strip()
            if msgDescodificada != '':
                break
            else:
                print('ERRO! Digite algo!')
        msgCodificada = codificar_mensagem(msgDescodificada)
        print(f'Mensagem passada pelo usuário: {msgDescodificada}')
        print(f'Mensagem codificada: {msgCodificada}')
        print('-'*tamanhoMsg)
        input('Pressione ENTER para continuar...')
    elif opcao == 2:
        Menu('Descodificar Mensagem')
        while True:
            msgCodificada = str(input('Digite ou cole a mensagem: ')).strip()
            if msgCodificada != '':
                break
            else:
                print('ERRO! Digite algo!')
        msgDescodificada = descodificar_mensagem(msgCodificada)
        print('Mensagem decodificada: {m}')
    
    else:
        Menu('Sair do Codificador')
        opcao = str(input('Você deseja sair do programa? [s/n]: ')).lower().strip()
        if opcao in 'simnaonão':
            print('Saindo...')
            exit()
        else:
            pass