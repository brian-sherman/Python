"""
Task 1
Complete the function to return the first two items in the given list

# Complete the function to return the first two items in the given list
def getFirstTwo(mylist):
# Student code goes here
 
# expected output: [8, 3]
print(getFirstTwo([8,3,5,2,10]))  
 
# expected output: [15, 2]
print(getFirstTwo([15,2,10,12]))

"""
def getFirstTwo(mylist):
    return mylist[0:2]
 
# expected output: [8, 3]
print(getFirstTwo([8,3,5,2,10]))  
 
# expected output: [15, 2]
print(getFirstTwo([15,2,10,12]))