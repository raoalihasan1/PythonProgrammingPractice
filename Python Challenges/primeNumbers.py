# Write a function to compute all prime numbers up to a given maximum value
def calcPrimesUpTo(maxVal: int):
    primeNumbers = []
    for X in range(2, maxVal):
        isPrime = True
        for Y in range(2, X):
            if X % Y == 0:
                isPrime = False
                break
        if (isPrime):
            primeNumbers.append(X)
    return primeNumbers


print(calcPrimesUpTo(15))
print(calcPrimesUpTo(25))
print(calcPrimesUpTo(50))
