# Write a function that performs position-based calculation for the checksum of a number of any length given as a string
def calcCheckSum(Digits: str):
    Sum = 0
    for X in range(len(Digits)):
        Sum += int(Digits[X]) * (X+1)
    return Sum % 10


print(calcCheckSum("11111"))
print(calcCheckSum("87654321"))
