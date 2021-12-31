from pycountry import countries

def tratErros(txtQuest, txtErro, type, numMax=150, numMin=0):
    while True:
        if type == 'int':
            try:
                variavel = int(input(txtQuest))

            except:
                print(txtErro)
        elif type == 'str':
            variavel = str(input(txtQuest))

while True:
    print('''       REGISTRATION FORM
    [ 1 ] Registrate
    [ 2 ] Login
    [ 3 ] Exit''')
    opcao = tratErros('Selecione uma opção: ', 'int', 1, 3)
