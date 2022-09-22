# Write a function which given an integer, converts the respective digits into corresponding text
def numberAsText(n: int):
    n = str(n)
    valueAsText = ""
    for X in range(len(n)):
        valueAsText += getStr(n[X]) + " "
    return valueAsText.strip()


def getStr(n: str):
    return {"0": "ZERO", "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR", "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE", "-": "MINUS"}[n]


print(numberAsText(7))
print(numberAsText(42))
print(numberAsText(13579))
print(numberAsText(-128))
