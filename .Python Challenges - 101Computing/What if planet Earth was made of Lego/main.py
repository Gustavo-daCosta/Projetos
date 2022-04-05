while True:
  try:
    terra = int(input('Digite o raio do planetóide (em Km): '))
  except:
    print('ERRO! Valor inválido, tente novamente')
  if (isinstance(terra, int) is True):
    break

# Volume do bloco de LEGO
width, length, height = 16, 16, 10
volume_block = width * length * height

terra = terra * 1000000
volume_terra = round((4/3) * 3.14 * (terra **3))
number = volume_terra/volume_block
print(f'{terra} mm')
print (f'{int(volume_terra)} mm³')
print(f'Caberiam {number:.0f} blocos de lego na terra')