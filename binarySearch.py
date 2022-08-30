from math import ceil as roundUp
import sys
import os
# Importing Function From Another Python File In This Repository
from Sorting import sortList


def findItem(Value, theList):
    midPoint = roundUp((len(theList)/2)) - 1
    if (theList[midPoint] == Value):
        return ("Found {} In The List".format(Value))
    elif (len(theList) == 1):
        return ("Could Not Find {} In The List".format(Value))
    else:
        if (theList[midPoint] < Value):
            return findItem(Value, theList[midPoint + 1:len(theList)])
        else:
            return findItem(Value, theList[0:midPoint])


sortCricketers = sortList(["Shaheen Afridi", "Aaron Finch", "Ben Stokes",
                           "Pat Cummins", "Virat Kohli", "Babar Azam", "Joe Root"])

sortIntegers = sortList([23, 1, 17, 2, 3, 19, 5, 7, 29, 11, 13, 29])

print("Before Sorting: " + str(["Shaheen Afridi", "Aaron Finch", "Ben Stokes",
                                "Pat Cummins", "Virat Kohli", "Babar Azam", "Joe Root"]), end="\n\n")

print("After Sorting: " + str(sortCricketers), end="\n\n")

print(findItem("James Anderson", sortCricketers))

print(findItem("Virat Kohli", sortCricketers), end="\n\n")

print("Before Sorting: " +
      str([23, 1, 17, 2, 3, 19, 5, 7, 29, 11, 13, 29]), end="\n\n")

print("After Sorting: " + str(sortIntegers), end="\n\n")

print(findItem(17, sortIntegers))

print(findItem(15, sortIntegers))
