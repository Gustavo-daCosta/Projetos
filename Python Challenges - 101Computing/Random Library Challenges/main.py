numInicial = 6
figura = 2
total = 11
razao = 5 + (2*(figura - 1))
formula = 5 + (figura - 1) * razao
for c in range(0, 100):
    print(f'Figura {figura}\t\ttotal {formula}\t\tnumero inicial {numInicial}\t\trazao {razao}')
    figura += 1
    total = 11 + numInicial
    razao = 5 + (2*(numInicial - 1))
    formula = 5 + (figura - 1) * razao
