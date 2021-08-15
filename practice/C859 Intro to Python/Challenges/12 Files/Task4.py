import os

# Complete the function to create the specified file and return the file name
def createFile(filename):
    f = open(filename, "w")
    f.write('test')
    f.close()
    return filename
 
# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))