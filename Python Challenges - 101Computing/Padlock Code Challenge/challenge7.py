code = 0

number = squareNumber = 0

while True:
    lastNumber = (number - 1) ** 2
    squareNumber = number**2
    number += 1
    if len(str(squareNumber)) == 4:
        squareNumber = lastNumber
        break


print(squareNumber) # OUTPUT: 961
# The code was correct!