code = 0

for digit1 in range(0, 10):
    for digit2 in range(0, 10):
        for digit3 in range(0, 10):
            if (digit1 == digit2 or digit1 == digit3 or digit2 == digit3):
                code += 1

print(f'Code: {code}')