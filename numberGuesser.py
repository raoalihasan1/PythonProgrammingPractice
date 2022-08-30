from random import randint as getInt


class numberGuesser:

    def __init__(self):
        self.__numberToGuess = getInt(1, 100)
        self.__guessesRemaining = 5
        self.__hintsRemaining = 2

    def userGuess(self, theGuess):
        if (theGuess == self.__numberToGuess):
            return "You Have Guessed Correctly!"
        else:
            self.__guessesRemaining -= 1
            if (self.__guessesRemaining == 0):
                return "You Have Failed To Guess Correctly! The Number Was {}".format(self.__numberToGuess)
            elif (theGuess < self.__numberToGuess):
                return "Wrong! Guess Higher"
            else:
                return "Wrong! Guess Lower"

    def getHint(self):
        hintString = ""
        if self.__hintsRemaining == 1:
            if self.__numberToGuess % 2 == 0:
                hintString += "The Number Is Even "
            else:
                hintString += "The Number Is Odd "
            for x in range(3, 12):
                if self.__numberToGuess % x == 0:
                    hintString += "And A Multiple Of {}".format(x)
                    break
        else:
            if self.__numberToGuess <= 25:
                hintString += "The Number Is 25 Or Below!"
            elif self.__numberToGuess > 25 and self.__numberToGuess < 50:
                hintString += "The Number Is Between 25 And 50 (Excluding Both Numbers)!"
            elif self.__numberToGuess >= 50 and self.__numberToGuess <= 75:
                hintString += "The Number Is Between 50 And 75 (Including Both Numbers)!"
            else:
                hintString += "The Number Is Greater Than 75!"
        self.__hintsRemaining -= 1
        return hintString

    def getNumberOfHints(self):
        return self.__hintsRemaining

    def getNumberOfAttempts(self):
        return self.__guessesRemaining


print("========== Welcome To Guess The Number ==========")
newGame = numberGuesser()
print("\n===================== Rules =====================\n1: The Number Being Guessed Is Between 1 And 100\n2: You Have 5 Chances To Guess The Number\n3: You Have 2 Hints Available\n=================================================\n")
print("========== I Have Thought Of A Number ===========")
while True:
    try:
        print("\nAttempts Remaining: {} - Hints Remaining: {}\n".format(
            newGame.getNumberOfAttempts(), newGame.getNumberOfHints()))
        usersGuess = int(input("Take A Guess: "))
        resultOfGuess = newGame.userGuess(usersGuess)
        print(resultOfGuess)
        if (resultOfGuess == "You Have Guessed Correctly!"):
            exit()
        else:
            if ("Failed" in resultOfGuess):
                exit()
            else:
                if (newGame.getNumberOfHints() > 0):
                    needHint = input(
                        "\nDo You Want A Hint? (Press Any Key Except N For Hint): ")
                    if needHint == "N" or needHint == "n":
                        continue
                    else:
                        print(newGame.getHint())
    except ValueError:
        print("Invalid Guess! Please Try Again")
