"""
# Complete the function to return a new list containing 
# the first two and last two items in the given list
def getFirstTwoAndLastTwo(mylist):
# Student code goes here
 
# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))
 
# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))

"""

# Complete the function to return a new list containing 
# the first two and last two items in the given list
def getFirstTwoAndLastTwo(mylist):
    newlist = []
    newlist = mylist[0:2] + mylist[-2:]
    return newlist
 
# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))
 
# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))