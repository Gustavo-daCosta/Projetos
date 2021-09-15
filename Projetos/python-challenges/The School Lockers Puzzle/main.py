lockers = [0] * 1000

for c in range(0, 1000):
    lockers[c] = 1

for c in range(0, 1000):
    for i in range(0, 1000, c+1):
        if lockers[i] == 0:
            lockers[i] = 1
        else:
            lockers[i] = 0

total = 1000
for c in range(0, 1000):
    total -= lockers[c]

print(f'Total number of lockers closed: {str(total)} lockers')