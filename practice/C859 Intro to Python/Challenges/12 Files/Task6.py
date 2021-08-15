import os

# Complete the function to return FILE if the given path is a file
# or return DIRECTORY if the given path is a directory
# or return NEITHER is it's not a file or directory
def whatIsIt(somePath):
    if os.path.isfile(somePath) == True:
        return 'FILE'
    elif os.path.isdir(somePath) == True:
        return 'DIRECTORY'
    else:
        return 'NEITHER'
 
# expected output: DIRECTORY
print(whatIsIt(os.getcwd()))
 
# expected output: FILE
print(whatIsIt(os.listdir(os.getcwd())[0]))
 
# expected output: NEITHER
print(whatIsIt('apple.pie.123.txt'))