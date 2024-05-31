from requests import get
import json

apiKey = 'e646bb457e1ae6babbc7afc1adb4526a'

while True:
    print('''           CONSULTA DO CLIMA
[ 1 ] - Consultar clima de uma cidade
[ 2 ] - Consultar clima de uma coordenada geográfica
[ 2 ] - Consultar clima de capitais pré-definidas
[ 3 ] - Ajuda
[ 4 ] - Sair''')
    while True:
        try:
            opcao = int(input('Digite a opção desejada: '))
        except ValueError:
            print('Opção inválida! Tente novamente')
        finally:
            if isinstance(opcao, int) is True and opcao in range(1, 5):
                break
    if opcao == 1:
        while True:
            try:
                cidade = input('Digite a cidade: ')
                break
            except ValueError:
                print('Cidade inválida! Tente novamente')
            finally:
                if isinstance(cidade, str) is True:
                    break
        request = get(f'api.openweathermap.org/data/2.5/weather?q={cidade}&appid={apiKey}?units=metric&lang=pt').json()
        for key, value in request.items():
            print(f'{key}: {value}')
    elif opcao == 2:
        while True:
            try:
                long = float(input('Digite a longitude: '))
                lat = float(input('Digite a latitude: '))
                break
            except ValueError:
                print('Coordenada inválida! Tente novamente')
        request = get(f'api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={apiKey}').json()
        for key, value in request.items():
            print(f'{key}: {value}')