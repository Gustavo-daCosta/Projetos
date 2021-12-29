while True:
    try:
        a = int(input('Enter a Number: '))
        b = int(input('Enter a Number: '))
    except:
        print('Error! Type a number.')
    finally:
        break

a = a + b
b = a + b
a = a - b

print(f'A: {a}')
print(f'B: {b}')