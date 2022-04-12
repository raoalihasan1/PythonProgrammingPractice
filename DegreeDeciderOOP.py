import re, time, sys

class Degree:

    studentCount = 0

    @classmethod
    def getName(cls, fullName):
        firstName, lastName = fullName.split(" ")
        return cls(firstName, lastName)

    def __init__(self, firstName, lastName):
        self.__fName = firstName
        self.__lName = lastName
        Degree.studentCount += 1

    def UniversityID(self, IDNum):
        self.__studentID = IDNum

    def DegreeLevel(self, Percentage):
        self.__DegreePercent = Percentage
        if int(Percentage) >= 70 :
            self.__DegreeType = "First-Class Honours"
        elif int(Percentage) >= 60 :
            self.__DegreeType = "Upper Second-Class Honours"
        elif int(Percentage) >= 50 :
            self.__DegreeType = "Lower Second-Class Honours"
        elif int(Percentage) >= 40 :
            self.__DegreeType = "Third-Class Honours"
        else :
            self.__DegreeType = "No Degree Achieved"

    def WriteToFile(self):
        TextFile = open("StudentsDegreeType.txt", "a+")
        TextFile.write("--------------------------------------------------\n")
        TextFile.write("Student Name: " + self.__fName + " " + self.__lName + "\n")
        TextFile.write("Student ID Number: " + self.__studentID + "\n")
        TextFile.write("Percentage: " + self.__DegreePercent + "% | Degree Type: " + self.__DegreeType + "\n")
        TextFile.write("--------------------------------------------------\n\n")
        TextFile.close()

def calculateStudentDegree():

    global Name
    Name = input("Enter Students Full Name: ")
    ValidateName = re.search("[a-zA-Z\s]+$", Name)

    while not ValidateName:
        print("This Is Not A Valid Name. Please Try Again")
        Name = input("Enter Students Full Name: ")
        ValidateName = re.search("[a-zA-Z\s]+$", Name)
        if ValidateName:
            break
        else:
            continue

    Name = Name.strip()
    IDAdder()
    PercentAdder()

def IDAdder():

    global ID
    ID = input("Enter The Students University ID: ")
    ID = ID.strip()
    with open('StudentsDegreeType.txt') as TxtFile:
        if ID in TxtFile.read():
            print("Degree Type Has Already Been Calculated For This Student")
            ExitYN()
        else:
            PercentAdder()

def PercentAdder():

    global Name, ID
    Percent = input("Enter The Final Percentage Achieved By The Student: ")
    Percent = Percent.strip()

    if Percent.endswith("%"):
        Percent.replace("%", "")
    elif Percent < 0 or Percent > 100:
        print("Percentage Is Invalid. Please Try Again!")
        PercentAdder()

    theStudent = Degree.getName(Name)
    theStudent.UniversityID(ID)
    theStudent.DegreeLevel(Percent)
    theStudent.WriteToFile()

    ExitYN()

def ExitYN():

    Exit = input("Do You Want To Exit [Y/N]: ")
    if(Exit.upper() == "Y" or Exit.upper() == "YES"):
        print("Number Of Students Added To Text File: " + str(Degree.studentCount))
        time.sleep(3)
        sys.exit()
    elif(Exit.upper() == "N" or Exit.upper() == "NO"):
        calculateStudentDegree()
    else:
        ExitYN()

print("------------Welcome To The UoM Degree Calculator Application------------")
calculateStudentDegree()