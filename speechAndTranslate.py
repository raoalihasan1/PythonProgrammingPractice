# Import All THe Required Modules
import pyttsx3
import uuid
import os
import googletrans
from googletrans import Translator
from time import sleep


# Create A Class Which Contains The Attributes And Methods To Translate, Convert Speech To Text And Save The Output
class speechAndTranslate:

    # Constructor That Takes The Users' Inputted Text As An Argument
    def __init__(self, theText: str):
        self.__Text = theText

    # Method That Converts Speech To Text And Saves It If The User Chooses To
    def convertToSpeech(self, saveYN: str):
        fileName = None
        initEngine = pyttsx3.init()
        initEngine.setProperty("rate", 175)
        initEngine.say(self.getText())
        if (saveYN == "Y"):
            try:
                fileName = "{}.wav".format(uuid.uuid4())
                initEngine.save_to_file(
                    self.getText(), fileName)
            except:
                print("\nFailed To Save The Text-To-Speech Audio - Please Try Again!\n")
        initEngine.runAndWait()
        # Synchronise The Program And Saving The File To Prevent Any Errors
        if (fileName != None):
            while (not os.path.isfile(fileName)):
                sleep(0.25)

    # Method That Prints The Translated Text
    def translateText(self, destLang: str):
        print("\nTranslated:", Translator().translate(
            self.getText(), dest=destLang).text)

    # Getter That Returns The Users' Inputted Text
    def getText(self):
        return self.__Text


# Method That Returns The Users' Choice Of What To Do
def getUserChoice():
    return input("\nSelect An Option From Below:\n1: Translate\n2: Text-To-Speech\n3: Exit\n\n")


if __name__ == "__main__":
    print("\n=== Welcome To Text-To-Speech And Translator ===")
    while True:
        userChoice = getUserChoice()
        getLang = None
        if (userChoice == "1"):
            getText = input("\nEnter The Text To Translate: ")
            while True:
                getLang = input("Enter The Language To Translate To: ").lower()
                try:
                    # Get The Key For The Target Language From Google Translates Dictionary
                    getLang = list(googletrans.LANGUAGES.keys())[list(
                        googletrans.LANGUAGES.values()).index(getLang)]
                    break
                except:
                    continue
        elif (userChoice == "2"):
            getText = input("\nEnter The Text To Convert To Speech: ")
            while True:
                saveYN = input(
                    "Do You Want To Save The Speech? (Y or N): ").upper()
                if (saveYN == "Y" or saveYN == "N"):
                    break
        elif (userChoice == "3"):
            exit()
        else:
            continue
        # Instantiate Objects And Call The Respective Methods Based On What The User Wishes To Do
        newObj = speechAndTranslate(getText)
        if (getLang == None):
            newObj.convertToSpeech(saveYN)
        else:
            newObj.translateText(getLang)
        continue
