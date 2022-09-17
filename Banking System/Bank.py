from time import sleep
from random import randint
from bankAccount import bankAccount


class Bank:

    __bankAccounts = []

    def getAllAccounts(self):
        return self.__bankAccounts

    def getNumOfAccounts(self):
        return len(self.__bankAccounts)

    def getItem(self, accountNum: str):
        for Accounts in self.__bankAccounts:
            if Accounts.getAccountNumber() == accountNum:
                return Accounts
        return None

    def addAccount(self, accoutNum: str, accountName: str):
        for Accounts in self.__bankAccounts:
            if Accounts.getAccountNumber() == accoutNum:
                return False
        self.__bankAccounts.append(bankAccount(accoutNum, accountName))
        return True

    def depositMoney(self, accountNum: str, Amount: float):
        for Accounts in self.__bankAccounts:
            if Accounts.getAccountNumber() == accountNum:
                if Accounts.depositAmount(Amount):
                    return True
        return False

    def withdrawMoney(self, accountNum: str, Amount: float):
        for Accounts in self.__bankAccounts:
            if Accounts.getAccountNumber() == accountNum:
                if Accounts.withdrawAmount(Amount):
                    return True
        return False

    def removeAccount(self, accountNum: str):
        for X in range(self.getNumOfAccounts()):
            if self.getAllAccounts()[X].getAccountNumber() == accountNum:
                if self.getAllAccounts().pop(X):
                    return True
        return False

    def displayOptions(self):
        while True:
            sleep(1)
            try:
                optionChosen = int(input(
                    "1: View All Accounts\n2: Deposit Amount\n3: Withdraw Amount\n4: Delete Account\n5: Add Account\n6: Search For Account\n7: Exit System\n\nSelect One Of The Following Options: "))
            except:
                print("Invalid Option Selected. Please Try Again!\n")
                continue
            if (optionChosen < 1 or optionChosen > 7):
                continue
            else:
                if (optionChosen == 1):
                    self.displayAccounts()
                if (optionChosen == 2):
                    self.displayDeposit()
                if (optionChosen == 3):
                    self.displayWithdraw()
                if (optionChosen == 4):
                    self.displayDelete()
                if (optionChosen == 5):
                    self.displayAdd()
                if (optionChosen == 6):
                    self.displaySearch()
                else:
                    exit()

    def displayAccounts(self):
        print("\n==== Displaying All Accounts ====")
        sleep(1)
        for Accounts in self.__bankAccounts:
            print("\n=================================\n")
            print("Account Name: {}".format(Accounts.getAccountName()))
            print("Account Number: {}".format(Accounts.getAccountNumber()))
            print("Account Balance: £{}".format(Accounts.getBalance()))
            sleep(0.5)
        print("\n=================================")
        print("Total Number Of Accounts: {}".format(self.getNumOfAccounts()))
        print("=================================\n")
        self.displayOptions()

    def displayDeposit(self):
        while True:
            try:
                accountNumber = input(
                    "\nEnter Acc. Number To Deposit To: ").upper()
                amountToDeposit = float(
                    input("\nEnter Amount To Deposit (In £): "))
                balanceBefore = self.getItem(accountNumber).getBalance()
                break
            except:
                print("Invalid Input. Please Try Again!\n")
                self.displayOptions()
        if (self.depositMoney(accountNumber, amountToDeposit)):
            print("\n=================================\nDeposited Into Account: {}".format(
                accountNumber))
            print("=================================\nBalance Before: £ {}\nBalance After: £ {}\n=================================\n".format(
                balanceBefore, self.getItem(accountNumber).getBalance()))
        else:
            print("\n=========================================\nFailed To Deposit £" + str(amountToDeposit)
                  + " Into The Account " + str(accountNumber)
                    + "\n=========================================\n")
        self.displayOptions()

    def displayWithdraw(self):
        while True:
            accountNumber = input(
                "\nEnter Acc. Number To Withdraw From: ").upper()
            try:
                amountToWithdraw = float(
                    input("\nEnter Amount To Withdraw (In £): "))
                balanceBefore = self.getItem(accountNumber).getBalance()
                break
            except:
                print("Invalid Input. Please Try Again!\n")
                self.displayOptions()
        if (self.withdrawMoney(accountNumber, amountToWithdraw)):
            print("\n=================================\nWithdrew From Account: {}".format(
                accountNumber))
            print("=================================\nBalance Before: £ {}\nBalance After: £ {}\n=================================\n".format(
                balanceBefore, self.getItem(accountNumber).getBalance()))
        else:
            print("\n=========================================\nFailed To Withdraw £" + str(amountToWithdraw)
                  + " From The Account " + str(accountNumber)
                    + "\n=========================================\n")
        self.displayOptions()

    def displayDelete(self):
        accountNumber = input(
            "\nEnter Acc. Number Of Account To Delete: ").upper()
        try:
            getAccount = self.getItem(accountNumber)
        except:
            print("Invalid Account Number. Please Try Again!\n")
            self.displayOptions()
        while True:
            getConfirmation = input(
                "Are You Sure You Want To Delete The Account Of {} (Y/N)? ".format(accountNumber)).upper()
            if (getConfirmation == 'Y'):
                sleep(0.5)
                if (self.removeAccount(accountNumber)):
                    print("\n=================================")
                    print("Deleted The Account With Number: {}".format(
                        accountNumber))
                    print("=================================\n")
                else:
                    print("\n=================================")
                    print("Failed To Delete The Account With Number: {}".format(
                        accountNumber))
                    print("=================================\n")
                break
            elif (getConfirmation == 'N'):
                print()
                break
        self.displayOptions()

    def displayAdd(self):
        accountName = input("\nEnter New Accountholder Name: ").upper()
        while True:
            getConfirmation = input(
                "Are You Sure You Want To Create An Account With Name {} (Y/N)? ".format(accountName)).upper()
            if (getConfirmation == 'Y'):
                sleep(0.5)
                if (self.addAccount(self.generateAccountNumber(), accountName)):
                    print("\n=================================\n")
                    print("Created New Account:\nAccount Number: {}\nAccount Name: {}\nBalance: £{}\n".format(self.getAllAccounts()[
                          self.getNumOfAccounts() - 1].getAccountNumber(), self.getAllAccounts()[self.getNumOfAccounts() - 1].getAccountName(),
                        self.getAllAccounts()[self.getNumOfAccounts() - 1].getBalance()))
                    print("=================================\n")
                else:
                    print("\n=================================")
                    print("Failed To Create New Account For: {}".format(accountName))
                    print("=================================\n")
                break
            elif (getConfirmation == 'N'):
                print()
                break
        self.displayOptions()

    def displaySearch(self):
        accountNumber = input(
            "\nEnter Acc. Number: ").upper()
        try:
            getAccount = self.getItem(accountNumber)
            sleep(0.5)
            print("\n=================================\n")
            print("Account Name: {}\nAccount Number: {}\nAccount Balance: £{}\n".format(
                getAccount.getAccountName(), getAccount.getAccountNumber(), getAccount.getBalance()))
            print("=================================\n")
        except:
            print("Invalid Account Number. Please Try Again!\n")
        finally:
            self.displayOptions()

    def generateAccountNumber(self):
        randomGen = "ABCDEFGHIJKLM01234NOPQRSTUVWXYZ567890"
        accountNum = ""
        for X in range(5):
            accountNum += randomGen[randint(0, len(randomGen) - 1)]
        return accountNum


Lloyds = Bank()
customerNames = ["Amna Illian", "Ben Aaron", "Lance Young",
                 "Joe Root", "Ali Hasan", "Sophie Clinch", "Jonathon Payne", "Ellyse Perry"]
for Customer in customerNames:
    Lloyds.addAccount(Lloyds.generateAccountNumber(), Customer.upper())
print("\n=== Welcome To The Management Of The Banking System ===\n")
Lloyds.displayOptions()
