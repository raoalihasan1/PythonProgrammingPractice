# Function That Loops Through The List (If Argument Is A List And All Elements Are Of The Same Type) And Sorts It By Comparing The Natural Sorting Order
def sortList(theList):
    if (type(theList) is list):
        Count = len(theList)
        try:
            while Count != 0:
                for x in range(len(theList) - 1):
                    if theList[x + 1] <= theList[x]:
                        tempStore = theList[x]
                        theList[x] = theList[x + 1]
                        theList[x + 1] = tempStore
                Count -= 1
        except:
            return "Cannot Sort Lists With Elements Of Different Types"
    return theList


print(sortList([3, 5, 2, 7, 1, 2, 8, 4, 6, 2, 9, 15, 18, 12, 0]))
print(sortList(["Hello", "My", "Name", "Is", "Ali", "Hasan"]))
print(sortList("I Am A String"))
print(sortList(10))
print(sortList(["Sort", "This", 1, 5, 9]), end="\n\n")
