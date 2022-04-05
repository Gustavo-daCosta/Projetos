from random import randint

lottery, user = list(), list()

while True:
    num = randint(1, 20)
    if num not in lottery:
        lottery.append(num)
    else:
        pass
    if len(lottery) == 6:
        break
lottery.sort()

for c in range(0, 6):
    while True:
        num = int(input('Enter a number between 1 and 20: '))
        if num >= 1 and num <= 20:
            user.append(num)
            break
        else:
            print('ERROR')

total = 0
for c in range(0, 6):
    if user[c] == lottery[c]:
        total += 1
if total == 6:
    print('CONGRATULATIONS! You hit all the numbers and won the lottery')
elif total > 0 and total < 6:
    print(f'You hit {total} numbers')
else:
    print('You didnt hit any number')