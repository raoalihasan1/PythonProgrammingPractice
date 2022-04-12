import sys, os

punctuations = '''!()-’[]{};:'",.?—…'''
englishtextpath = sys.argv[1]
inputpath = sys.argv[2]

if inputpath.endswith("/"):
    pass
else:
    inputpath += "/"
outputpath = sys.argv[3]  

if outputpath.endswith("/"):
    pass
else:
    outputpath += "/"

if not os.path.exists(outputpath):
    os.makedirs(outputpath)

for filepath in os.listdir(inputpath):
    if filepath.endswith(".txt"):
        punctuationremoved, uppercaseremoved, numbersremoved, totalwords, correctwords = 0, 0, 0, 0, 0
        fileinput = os.path.join(inputpath, filepath)
        file = open(fileinput)
        text = file.read()
        if "\n" in text:
            text = text.replace("\n","")
        ellipsescount = text.count("...")
        
        # formatting
        for char in text:
            if char.isdigit():
                text = text.replace(char, "")
                numbersremoved += 1
            if char in punctuations:
                text = text.replace(char, "")
                punctuationremoved += 1
            if char.isupper():
                text = text.replace(char, char.lower())
                uppercaseremoved += 1
        punctuationremoved = punctuationremoved - (2*ellipsescount)

        # spellchecking
        spellchecktest = text.split(" ")
        engFile = open(englishtextpath)
        engFileList = engFile.readlines()
        EngWords = []
        for x in engFileList:
            EngWords.append(x.rstrip())
        engFile.close()
        for x in range(len(spellchecktest)):
            if spellchecktest[x]:
                for y in EngWords:
                    if spellchecktest[x] == y:
                        correctwords += 1  
                totalwords += 1
        incorrectwords = totalwords - correctwords
        filepath = filepath.replace(".txt","_output.txt")
        fileoutput = os.path.join(outputpath, filepath)  
        outputfile = open(fileoutput, "w")
        outputfile.write("Formatting ###################\n")
        outputfile.write("Number of upper case letters changed: " + str(uppercaseremoved) + "\n")
        outputfile.write("Number of punctuations removed: " + str(punctuationremoved) + "\n")
        outputfile.write("Number of numbers removed: " + str(numbersremoved) + "\n")
        outputfile.write("Spellchecking ###################\n")
        outputfile.write("Number of words: " + str(totalwords) + "\n")
        outputfile.write("Number of correct words: " + str(correctwords) + "\n")
        outputfile.write("Number of incorrect words: " + str(incorrectwords))
        outputfile.close()
        file.close()
        
