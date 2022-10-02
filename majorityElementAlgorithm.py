# Input: An array of integers A, of length n
# Output: An integer k such that k appears in more than half of the positions of A if such a k exists. Otherwise "No"

def majorityElement(A: list):
    numCount = 0
    for x in range(len(A)):
        for y in range(len(A)):
            if A[x] == A[y]:
                numCount += 1
        if(numCount > (len(A) / 2)):
            return A[x]
        numCount = 0
    return "No"

print("Algorithm With O(n^2) Complexity Using Nested For Loop")
print(majorityElement([1, 1, 1, 8, 6, 1, 4]))
print(majorityElement([7, 5, 5, 3, 5, 5, 2]))
print(majorityElement([1, 2, 3, 4, 5, 6, 6]), end = "\n--\n")

def majorityElementEfficient(A: list):
    posCount, numCount, I = 0, 0, 0
    listMode = A[0]
    while True:
        if(A[posCount] == listMode):
            numCount += 1
        if(numCount > (len(A) / 2)):
            return listMode
        if(posCount == len(A) - 1):
            if(I == len(A) - 1):
                break
            else:
                I += 1
                listMode = A[I]
                posCount, numCount = 0, 0
                continue
        posCount += 1
    return "No"

print("Algorithm With O(n) Complexity Using Single While Loop")
print(majorityElementEfficient([1, 1, 1, 8, 6, 1, 4]))
print(majorityElementEfficient([7, 5, 5, 3, 5, 5, 2]))
print(majorityElementEfficient([1, 2, 3, 4, 5, 6, 6]))
