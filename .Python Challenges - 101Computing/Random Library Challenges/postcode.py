#Your task is to write a Python script to generates a random UK postcode in the format: LetterLetterNumber_NumberLetterLetter.
from random import randint

postcode = ''

for position in range(0, 7):
    if position == 2 or position == 4:
        postcode += str(randint(0, 9))
    elif position == 3:
        postcode += ' '
    else:
        postcode += str(chr(randint(65, 90)))

print(f'Postcode: {postcode}')