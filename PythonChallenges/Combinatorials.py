# Compute all combinations of the values of a, b and c (each starting from 1 and less than 100) for which the following formula holds: a^2 + b^2 = c^2
def calcCombinatorials():
    for X in range(1, 100):
        for Y in range(1, 100):
            for Z in range(1, 100):
                if X ** 2 + Y ** 2 == Z ** 2:
                    print("a = {}, b = {}, c = {}".format(X, Y, Z))


calcCombinatorials()
