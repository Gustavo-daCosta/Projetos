# Your task is to write a Python script to randomly pick and output a card from a deck of 52 playing cards. 
# The program should output the suit and value of the card (e.g. 7 of hearts, Queen of clubs, etc…).

from random import choice

value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

card = f'{choice(value)} of {choice(suit)}'
print(f'Pick a card: {card}')