# Write a recursive function that computes fibonacci numbers
from mimetypes import init


def fibRec(n: int):
    if n == 1 or n == 2:
        return 1
    else:
        return fibRec(n - 1) + fibRec(n - 2)


print("Fibonacci Using Recursion")
for X in range(1, 9):
    print(fibRec(X))
print("-------------------------")


# Write an iterative function that computes fibonacci numbers
def fibIterate(n: int):
    firstVal = 1
    secondVal = 1
    Total = 1
    for X in range(2, n):
        Total = firstVal + secondVal
        firstVal = secondVal
        secondVal = Total
    return Total


print("Fibonacci Using Iteration")
for X in range(1, 9):
    print(fibIterate(X))
