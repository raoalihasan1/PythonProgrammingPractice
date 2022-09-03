# Task 1: Given An Integer ( + Or - ), Return The Integer With Reversed Digits


def intReverse(X: int):
    X = str(X)
    if X[0] == "-":
        return int("-" + X[:0:-1])
    return int(X[:: -1])


print("TASK 1:\n")
print(intReverse(-12))
print(intReverse(31))
print(intReverse(7))
print(intReverse(-3), end="\n\n")

# For A Given Sentence, Return The Average Word Length After Removing Punctuation


def averageWordLength(X: str):
    thePunctuation = [",", "\"", "?", ".", "!", "'", ":", ";", "(", ")"]
    for Punctuation in thePunctuation:
        if Punctuation in X:
            X = X.replace(Punctuation, '')
    X = X.split(" ")
    averageLength = 0
    wordCount = 0
    for Word in X:
        averageLength += len(Word)
        wordCount += 1
    return round(averageLength / wordCount, 2)


print("TASK 2:\n")
print(averageWordLength("Hi all, my name is Tom...I am originally from Australia."))
print(averageWordLength(
    "Currently, I am studying at the university of manchester doing a BSc (Hons) in computer science."))
print(averageWordLength(
    "I need to work very hard to learn more about algorithms in python!"), end="\n\n")


# Given An Array Of Integers, Determine Whether The Array Is Monotonic Or Not


def monotonicArray(X: list):
    startNum = X[0]
    Increasing = True
    for x in range(1, len(X)):
        if (startNum > X[x]):
            Increasing = False
        elif (startNum < X[x] and not Increasing):
            return False
        startNum = X[x]
    return True


print("TASK 3:\n")
print(monotonicArray([6, 5, 4, 4]))
print(monotonicArray([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(monotonicArray([1, 1, 2, 3, 7]), end="\n\n")


# Given An Array Of Numbers, Write A Function To Move All Zeroes To The
# End Of It While Maintaining The Relative Order Of The Non-Zero Elements


def moveZeroToListEnd(X: list):
    returnList = []
    xCount = 0
    for x in X:
        if x == 0:
            xCount += 1
        else:
            returnList.append(x)
    while xCount != 0:
        returnList.append(0)
        xCount -= 1
    return returnList


print("TASK 4:\n")
print(moveZeroToListEnd([0, 1, 0, 3, 12]))
print(moveZeroToListEnd([0, 6, 2, 4, 0, 0, 9, 8, 0]))
print(moveZeroToListEnd([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]), end="\n\n")


# Given An Array Containing None Values, Fill In The None Values With Most Recent Non None Values In The Array


def replaceNone(X: list):
    for x in range(1, len(X)):
        if X[x] == None:
            X[x] = X[x - 1]
    return X


print("TASK 5:\n")
print(replaceNone([1, None, 2, 3, None, None, 5, None]))
print(replaceNone([None, 2, None, 5, 7, 8, None, None, 3]), end="\n\n")


# Given Two Sentences, Return An Array That Has Words That Appear
# In One Sentence But Not The Other And An Array With Common Words


def Sentences(X: str, Y: str):
    commonWords, differentWords = [], []
    X = X.split()
    Y = Y.split()
    for x in X:
        if x in Y:
            commonWords.append(x)
        else:
            differentWords.append(x)
    for y in Y:
        if y not in X and y not in differentWords:
            differentWords.append(y)
    return (list(differentWords), list(commonWords))


print("TASK 6:\n")
print(Sentences("We are really pleased to meet you in our city",
      "The city was hit by a really heavy storm"), end="\n\n")


# Write A program To Print All Prime Numbers In An Interval


def primeNumbers(X: int):
    primeList = []
    for x in range(2, X):
        isPrime = True
        for y in range(2, x):
            if x % y == 0:
                isPrime = False
        if isPrime:
            primeList.append(x)
    return primeList


print("TASK 7:\n")
print(primeNumbers(50))
