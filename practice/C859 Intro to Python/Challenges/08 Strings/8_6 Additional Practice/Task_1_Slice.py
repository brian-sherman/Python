# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
    str_x = mystring[:x]
    print(str_x)
 
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)