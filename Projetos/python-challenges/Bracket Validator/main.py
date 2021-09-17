expression = str(input('Type the arithmetic expression: '))
lista = expression.split()
closed = opened = 0
operations = '+-//**'
Justification = 'Your arithmetic expression is valid!'

def verification(bracket):
    global valid, Justification
    local = lista.index(bracket)
    if local == 0:
        if lista[local+1] in operations:
            Justification = 'Invalid use of brackets'
    elif local == (len(lista))-1:
        if lista[local-2] in operations:
            Justification = 'Invalid use of brackets'
    else:
        if lista[local+1] in operations or lista[local-2] in operations:
            Justification = 'Invalid use of brackets'
    lista.remove(bracket)
    if Justification == 'Invalid use of brackets':
        valid = False
    else:
        valid = True
    
while True:
    if lista[0] == ')' or lista[(len(lista)-1)] == '(':
        Justification = 'Invalid use of brackets'
        break
    if '(' in lista:
        opened += 1
        verification()
        if valid is False:
            break
        lista.remove('(')
    elif ')' in lista:
        closed += 1
        verification()
        if valid is False:
            break
        lista.remove(')')
    else:
        break

print(Justification)