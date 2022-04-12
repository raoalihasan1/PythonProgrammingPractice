import sys, os
inputpath = sys.argv[1]
if inputpath.endswith("/"):
    pass
else:
    inputpath += "/"
outputpath = sys.argv[2]  
if outputpath.endswith("/"):
    pass
else:
    outputpath += "/"
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
for filepath in os.listdir(inputpath):
    if filepath.endswith(".txt"):
        fileinput = os.path.join(inputpath, filepath)  
        morseCode = {
            ".-" : "A",
            "-..." : "B",
            "-.-." : "C",
            "-.." : "D",
            "." : "E",
            "..-." : "F",
            "--." : "G",
            "...." : "H",
            ".." : "I",
            ".---" : "J",
            "-.-" : "K",
            ".-.." : "L",
            "--" : "M",
            "-." : "N",
            "---" : "O",
            ".--." : "P",
            "--.-" : "Q",
            ".-." : "R",
            "..." : "S",
            "-" : "T",
            "..-" : "U",
            "...-" : "V",
            ".--" : "W",
            "-..-" : "X",
            "-.--" : "Y",
            "--.." : "Z",
            ".----" : "1",
            "..---" : "2",
            "...--" : "3",
            "....-" : "4",
            "....." : "5",
            "-...." : "6",
            "--..." : "7",
            "---.." : "8",
            "----." : "9",
            "-----" : "0",
            ".-.-.-" : ".",
            "--..--" : ",",
            "..--.." : "?",
            ".----." : "'",
            "-..-." : "/",
            "---..." : ":",
            "-.-.-." : ";",
            ".-.-." : "+",
            "-....-" : "-",
            "-...-" : "=",
            ".-..-." : "’",
            "-.-.--" : "!",
            "-.--." : "(",
            "-.--.-" : ")",
            ".-..-."    : "’"
        }
        punctuations = '''!()-’[]{};:'",.?—…'''
        file = open(fileinput)
        text = file.read()
        if "\n" in text:
            text = text.replace("\n", "")
        file.close()
        plaintext = ""
        CipherTextPosition = 0
        if text[0] == "h" or text[0] == "H":
            text = text.split(":")
            text.pop(0)
            text = ''.join(str(x) for x in text)
            text = text.split(" ")
            for i in text:
                plaintext += bytearray.fromhex(i).decode()
            filepath = filepath.replace(".txt","_output.txt")
            fileoutput = os.path.join(outputpath, filepath)  
            outputfile = open(fileoutput, "w")
            outputfile.write(plaintext.lower())
            outputfile.close()
        elif text[0] == "c" or text[0] == "C":
            text = text.split(":")
            text.pop(0)
            text = ''.join(str(x) for x in text)
            for x in text:
                if x == ' ':
                    plaintext += ' '
                else:
                    if x in punctuations:
                        plaintext += x
                    elif x == "a":
                        plaintext += "x"
                    elif x == "b":
                        plaintext += "y"
                    elif x == "c":
                        plaintext += "z"
                    else:
                        ASCIIEquivalent = ord(x)
                        ASCIIEquivalent -= 3
                        plaintext += chr(ASCIIEquivalent)
            filepath = filepath.replace(".txt","_output.txt")
            fileoutput = os.path.join(outputpath, filepath)  
            outputfile = open(fileoutput, "w")
            outputfile.write(plaintext.lower())
            outputfile.close()
        elif text[0] == "m" or text[0] == "M":
            text = text.split(":")
            text.pop(0)
            text = ''.join(str(x) for x in text)
            for i in text:
                if i == "/":
                    text = text.replace(i, "")
            text = text.split(' ')
            for i in text:
                if i in morseCode:
                    plaintext += morseCode[i]
                else:
                    plaintext += ' '
            filepath = filepath.replace(".txt","_output.txt")
            fileoutput = os.path.join(outputpath, filepath) 
            outputfile = open(fileoutput, "w")
            outputfile.write(plaintext.lower())
            outputfile.close()
