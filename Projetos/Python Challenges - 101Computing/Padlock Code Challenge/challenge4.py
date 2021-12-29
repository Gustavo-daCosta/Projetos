code = 0

for digit1 in range(0, 10):
    for digit2 in range(0, 10):
        for digit3 in range(0, 10):
            number = digit1 + digit2 + digit3
            if number % 2 == 0:
                pass
            else:
                code += 1

print(f'Code: {code}')