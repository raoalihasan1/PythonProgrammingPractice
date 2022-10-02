# You are running a summer camp for children and are put in charge of See Saw.
# This is most fun when children on both sides are equal weight.
# Your solution is to give each child a hat of varying weight to balance out them out.
# To help you in this task you need to devise an algorithm that takes the weight of two children and the weights of the available hats and works out which hats to give to each child.
# Input: A pair of numbers (left, right) and a list of hat weights W of length n
# Output: A different pair of numbers (W[i], W[j]) such that left + W[i] = right + W[j] or "Not Possible" if there are no such i and j 
def balanceSeeSaw(pairs: list, W: list):
    for i in range(len(W)):
        for j in range(i, len(W)):
            if(W[i] + pairs[0] == W[j] + pairs[1]):
                return [W[i], W[j]]
    return "Not Possible"

print("Algorithm With O(n^2) Complexity Using Nested For Loop")
print(balanceSeeSaw([12, 5], [4, 9, 11]))
print(balanceSeeSaw([12, 5], [9, 8, 5]))
print(balanceSeeSaw([7, 3], [3, 4, 9, 7]), end = "\n------\n")

def balanceSeeSawEfficient(pairs: list, W: list):
    W = sorted(W)
    i = 0
    j = len(W) - 1
    while(j != 0):
        if W[i] + pairs[0] == W[j] + pairs[1]:
            return [W[i], W[j]]
        else:
            if(i == j):
                i = 0
                j -= 1
            else:
                i += 1
    return "Not Possible"

print("Algorithm With O(n log n) Complexity Using Sort")
print(balanceSeeSawEfficient([12, 5], [4, 9, 11]))
print(balanceSeeSawEfficient([12, 5], [9, 8, 5]))
print(balanceSeeSawEfficient([7, 3], [3, 4, 9, 7]))
