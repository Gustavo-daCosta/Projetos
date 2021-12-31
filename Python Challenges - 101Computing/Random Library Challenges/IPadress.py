# An IP address consists of 4 numbers between 0 and 255 separated by a dot. 
# Your task is to write a Python script that generates and outputs a valid random IP address.

from random import randint

IPadress = ''
for c in range(0, 4):
    num = randint(0, 255)
    if c < 3:
        IPadress += str(num) + '.'
    else:
        IPadress += str(num)

print(f'IP Adress: {IPadress}')