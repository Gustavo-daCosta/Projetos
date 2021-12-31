code = 0
for digit1 in range(0, 10):
    for digit2 in range(0, 10):
        for digit3 in range(0, 10):
            print(str(digit1)+str(digit2)+str(digit3))
            if digit1 < digit2 and digit2 < digit3:
                code += 1

print(f"Code: {code}")