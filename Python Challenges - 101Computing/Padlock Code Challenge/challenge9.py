primesTotal = numberOfPrimes = 0
def isPrime(number):
    global primesTotal, numberOfPrimes
    prime = True
    for c in range(2, number):
        if number % c == 0:
            prime = False
    if prime is True:
        primesTotal += number
        numberOfPrimes += 1

code = counter = 0
for c in range(0, 1000):
    isPrime(c)
numberOfPrimes -= 2
primesTotal -= 1
code = round(primesTotal / numberOfPrimes)

print(f'Code: {code}') # OUTPUT: 453
# The code was correct