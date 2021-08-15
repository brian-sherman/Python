import os

# Complete the function to print all files in the given directory
def printFiles(someDirectory):
    for dirname, subdir, file in os.walk(someDirectory):
        print(file)
    
# expected output: main.py    
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())