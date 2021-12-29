from keyboard import is_pressed
from time import sleep

while True:
    try:
        if is_pressed('tab'):
            print('Pressionou!')
            sleep(0.1)
            break
    except:
        print('Não pressionou.')