plainText = input("Enter The String To Encrypt: ").upper()

cipherText = ""

Alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintextPosition = 0

while plaintextPosition < len(plainText):

	plaintextChar = plainText[plaintextPosition]

	alphabetPosition = 3

	while plaintextChar != Alphabet[alphabetPosition]:

		alphabetPosition += 1

	alphabetPosition -= 3

	cipherText = cipherText + Alphabet[alphabetPosition]

	plaintextPosition += 1

print("The Encrypted String Is " + str(cipherText))
