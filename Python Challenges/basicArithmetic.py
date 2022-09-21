# Write a function that multiplies two variables, divides their product by two, and outputs the remainder with respect to division by 7
def Calculation(m: int, n: int):
    return int(((m * n) / 2) % 7)


print(Calculation(6, 7))
print(Calculation(5, 5))
