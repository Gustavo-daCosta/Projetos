# Your task is to write a Python script to generates a random phone number consisting of 11 digits.

from random import randint

number = ''
for c in range(0, 11):
    number += str(randint(0, 9))

print(f'Phone number generated: {number}')