from random import choice
from string import digits


class Student:

    __yearPercentages = []
    __allStudents = []

    def __init__(self, studentName, studentAge, studentIDNumber, yearOfStudy=1):
        self.__Name = studentName
        self.__Age = studentAge
        self.__IDNumber = studentIDNumber
        self.__studyYear = yearOfStudy
        self.addStudents(self)

    def getStudentName(self):
        return self.__Name

    def getStudentAge(self):
        return self.__Age

    def getStudentIDNumber(self):
        return self.__IDNumber

    def getYearOfStudy(self):
        return self.__studyYear

    def setStudentName(self, studentName):
        self.__Name = studentName

    def setStudentAge(self, studentAge):
        self.__Age = studentAge

    def setStudentIDNumber(self, studentIDNumber):
        self.__IDNumber = studentIDNumber

    def setStudentIDNumber(self, yearOfStudy):
        self.__studyYear = yearOfStudy

    def addYearPercentages(self, Percentage):
        try:
            Percentage = float(str(Percentage))
            if(Percentage > 100 or Percentage < 0):
                print("You Have Inputted An Invalid Number")
            else:
                self.__yearPercentages.append(Percentage)
        except ValueError:
            print("You Have Inputted An Invalid Number")

    def getYearPercentages(self):
        return self.__yearPercentages

    def printStudentDetails(self):
        print("\n-----------------------------------")
        print("Student Name:", self.__Name)
        print("Student Age:", self.__Age)
        print("Student Number:", self.__IDNumber)
        print("Year Of Study:", self.__studyYear)
        for x in range(len(self.__yearPercentages)):
            print("Year " + str(x + 1) + " Percentage: " +
                  str(self.__yearPercentages[x]) + "%")
        print("-----------------------------------\n")

    @classmethod
    def addStudents(cls, self):
        cls.__allStudents.append(self)

    @classmethod
    def deleteStudents(cls, self):
        cls.__allStudents.remove(self)

    @classmethod
    def getAllStudents(cls):
        return cls.__allStudents


def mainMenu():
    userChoice = getUserChoice()
    while(userChoice != "x"):
        try:
            userChoice = int(str(userChoice))
            if(userChoice > 4 or userChoice < 1):
                print("You Have Inputted An Invalid Option")
                userChoice = getUserChoice()
            else:
                if userChoice == 1:
                    getNewStudentDetails()
                elif userChoice == 2:
                    studentDetails(True)
                elif userChoice == 3:
                    studentDetails(False)
                elif userChoice == 4:
                    getTotalNumOfStudents()
            break
        except ValueError:
            print("You Have Inputted An Invalid Option")
            userChoice = getUserChoice()
    exit()


def getUserChoice():
    userChoice = input(
        "Choose An Option:\n1. Add New Student\n2. View A Student Details\n3. Delete A Student\n4. Get Total Number Of Students\nPress X To Exit\n\n")
    return userChoice.lower()


def generateUniqueID():
    idList = list()
    idExists = False
    for x in range(6):
        idList.append(choice(digits))
    allStudents = Student.getAllStudents()
    for theStudent in allStudents:
        if(theStudent.getStudentIDNumber() == ''.join(idList)):
            idExists = True
            break
    if(idExists):
        generateUniqueID()
    else:
        return ''.join(idList)


def getNewStudentDetails():
    print("\n-----------------------------------")
    studentName = input("Enter Student Name: ")
    while True:
        try:
            studentAge = int(input("Enter Student Age: "))
            if(studentAge <= 0):
                print("Invalid Age! Please Try Again.")
                continue
        except ValueError:
            print("Invalid Age! Please Try Again.")
            continue
        else:
            break

    while True:
        try:
            yearOfStudy = int(input("Enter Year Of Study: "))
            if(yearOfStudy > 6 or yearOfStudy < 0):
                print("Invalid Year Of Study! Please Try Again.")
                continue
        except ValueError:
            print("Invalid Year Of Study! Please Try Again.")
            continue
        else:
            break
    createID = generateUniqueID()
    Student(studentName.strip().title(), studentAge,
            createID, yearOfStudy)
    print("-----------------------------------")
    print("Added Student! Assigned ID", createID)
    print("-----------------------------------\n")
    mainMenu()


def studentDetails(Get):
    print("\n-----------------------------------")
    studentID = input("Enter Student ID Number: ")
    print("-----------------------------------")
    studentFound = False
    allStudents = Student.getAllStudents()
    for theStudent in allStudents:
        if(theStudent.getStudentIDNumber() == studentID):
            if(Get):
                print(theStudent.printStudentDetails())
            else:
                Student.deleteStudents(theStudent)
                print(
                    "\n-----------------------------------\nStudent Deleted!\n-----------------------------------\n")
            studentFound = True
            break
    if(not studentFound):
        print("\n-----------------------------------\nStudent Not Found!\n-----------------------------------\n")
    mainMenu()


def getTotalNumOfStudents():
    print("\n-----------------------------------")
    print("Total Number Of Students:", len(Student.getAllStudents()))
    print("-----------------------------------\n")
    mainMenu()


print("\n-----------------------------------\nWelcome To The Student System\n-----------------------------------\n")
mainMenu()
