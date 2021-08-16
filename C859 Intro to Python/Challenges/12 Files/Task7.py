import os

# Complete the function to read the contents of the specified file and print the contents
def printFileContents(filename):
    f = open(filename, 'r')
    print(f.read())
    f.close()
 
# expected output: Hello
with open("test.txt", 'w') as f: 
    f.write("Hello")
printFileContents("test.txt")