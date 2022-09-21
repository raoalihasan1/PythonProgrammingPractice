# Write a function that counts as well as sums up the natural numbers that are divisible by 2 or 7 up to a given maximum value (exclusive)
def calcSumAndCountAllNumbersDivBy2or7(maxVal: int):
    Total = 0
    Counter = 0
    for X in range(1, maxVal):
        if X % 2 == 0 or X % 7 == 0:
            Counter += 1
            Total += X
    return [Counter, Total]


print("Result Count: {}\nSum: {}\n".format(
    calcSumAndCountAllNumbersDivBy2or7(3)[0], calcSumAndCountAllNumbersDivBy2or7(3)[1]))
print("Result Count: {}\nSum: {}\n".format(
    calcSumAndCountAllNumbersDivBy2or7(8)[0], calcSumAndCountAllNumbersDivBy2or7(8)[1]))
print("Result Count: {}\nSum: {}\n".format(
    calcSumAndCountAllNumbersDivBy2or7(15)[0], calcSumAndCountAllNumbersDivBy2or7(15)[1]))
