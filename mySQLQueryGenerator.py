import csv


# Reads Each Row Of CSV Into List And Returns The List
def readCSV(fileName: str):
    rowsList = []
    with open(fileName, "r") as theFile:
        readFile = csv.reader(theFile)
        for X in readFile:
            rowsList.append(X)
    return rowsList


# Generates Insert Query Using The Rows From CSV
def insertQueryFromCSV(tableName: str, fileName: str):
    fileRows = readCSV(fileName)
    tableHeaders = ",".join(fileRows[0])
    valuesToInsert = []
    for X in fileRows[1:]:
        valuesToInsert.append("\t({})".format(",".join(X)))
    return "INSERT INTO {} ({}) VALUES\n {};".format(tableName, tableHeaders, ",\n".join(valuesToInsert))


# Generates An Insert Query Using The Passed Arguments
def insertQuery(tableName: str, tableHeaders: str, theValues):
    return f"INSERT INTO {tableName} ({tableHeaders}) VALUES\n ({theValues});"


# Generates A Select Query Using The Passed Arguments
def selectQuery(tableName: str, whatToSelect: str, theCondition=1):
    return f"SELECT {whatToSelect} FROM {tableName} WHERE {theCondition};"


# Generates An Update Query Using The Passed Arguments
def updateQuery(tableName: str, valuesToUpdate: str, theCondition: str):
    return f"UPDATE {tableName} SET {valuesToUpdate} WHERE {theCondition};"


# Generates A Delete Query Using The Passed Arguments
def deleteQuery(tableName: str, theCondition=1):
    return f"DELETE FROM {tableName} WHERE {theCondition};"


# Testing The Different Functions
print(insertQueryFromCSV("Medical", "medicalInsurance.csv"), end="\n\n")
print(insertQuery("Users", "Email, Gender",
      "alirao2880@gmail.com, Male"), end="\n\n")
print(selectQuery("Users", "Username, Email",
      "Username = 'Ali_Hasan1'"), end="\n\n")
print(selectQuery("Users", "Username, Email", 1), end="\n\n")
print(updateQuery("Users", "Username='Ali_Hasan1'",
      "Email='alirao2880@gmail.com'"), end="\n\n")
print(deleteQuery("Users", "Username='Ali_Hasan1'"), end="\n\n")
print(deleteQuery("Users"))
