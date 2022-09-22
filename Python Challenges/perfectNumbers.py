# By definition, a natural number is a perfect number if its value is equal to the sum of its real divisors.
# Write a function that calculates the perfect numbers up to a maximum value
def calcPerfectNumber(maxVal: int):
    perfectNumbers = []
    for X in range(1, maxVal):
        tempList = []
        for Y in range(1, X):
            if X % Y == 0:
                tempList.append(Y)
        if (sum(tempList)) == X:
            perfectNumbers.append(X)
    return perfectNumbers


print(calcPerfectNumber(1000))
print(calcPerfectNumber(10000))
