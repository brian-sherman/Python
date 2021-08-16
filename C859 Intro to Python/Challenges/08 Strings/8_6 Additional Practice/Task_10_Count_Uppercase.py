# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
    x = 0
    l = list(mystring)
    for char in l:
        if char.isupper() == True:
            x += 1
    return x

 
# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary'))