plainText = input("Enter The String To Encrypt: ").upper()

cipherText = ""

Alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

for eachChar in plainText:

    for x in range(len(Alphabet)):

        if Alphabet[x] == eachChar:

            cipherText += Alphabet[x - 3]

    if eachChar == " ":

        cipherText += " "


print("The Encrypted String Is " + str(cipherText))
