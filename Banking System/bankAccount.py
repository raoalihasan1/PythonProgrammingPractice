class bankAccount:

    def __init__(self, accountNumber: str, accountName: str):
        self.__accountNumber = accountNumber
        self.__accountName = accountName
        self.__Balance = 0.00

    def getAccountNumber(self):
        return self.__accountNumber

    def getAccountName(self):
        return self.__accountName

    def getBalance(self):
        return round(self.__Balance, 2)

    def depositAmount(self, Amount: float):
        currentBalance = self.__Balance
        self.__Balance += round(Amount, 2)
        if (currentBalance != self.__Balance):
            return True
        return False

    def withdrawAmount(self, Amount: float):
        if ((self.__Balance - Amount) < 0):
            return False
        currentBalance = self.__Balance
        self.__Balance -= round(Amount, 2)
        if (currentBalance != self.__Balance):
            return True
        return False
