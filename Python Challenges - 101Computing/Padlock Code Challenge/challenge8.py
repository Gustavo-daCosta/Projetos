def isPrime(number):
    prime = True
    global code
    for c in range(2, number):
        if number % c == 0:
            prime = False
    if prime is True and len(str(number)) == 3:
        code = number

code = counter = 0
while True:
    isPrime(counter)
    if counter == 1000:
        break
    counter += 1

print(code) # OUTPUT: 997
# The code was correct!