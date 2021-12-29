code = 0

for digit1 in range(0, 10):
    for digit2 in range(0, 10):
        for digit3 in range(0, 10):
            if (digit1 %2 == 0) and (digit2 %2 == 0) and (digit3 %2 == 0):
                code += 1

print(f'Code: {code}')