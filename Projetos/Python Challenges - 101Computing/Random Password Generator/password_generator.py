from random import randint

punctuation_ASCII = [128, 163, 165, 36, 169, 153, 176, 152, 161, 191, 33, 34, 35, 36, 37, 38, 61, 63, 64, 95]

password = ''

for c in range(0, 2):
    password += chr(randint(65, 90)) + chr(randint(97, 122)) + chr(randint(48, 57)) + chr(punctuation_ASCII[randint(0, 19)])
print(f'Password: {password}')