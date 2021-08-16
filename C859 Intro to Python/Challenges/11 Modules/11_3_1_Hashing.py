"""
from hashlib import md5, sha1

text = input("Enter text to hash ('q' to quit): ")

while text != 'q':
    algorithm = input('Enter algorithm (md5/sha1): ')
    if algorithm == 'md5':
        output = md5(text.encode('utf-8'))
    elif algorithm == 'sha1':
        output = sha1(text.encode('utf-8'))
    else:
        output = 'Invalid algorithm selection'
    print('Hash value:', output.hexdigest())

    text = input("\nEnter text to hash ('q' to quit): ")


Improve the hashing example from above by adding a new algorithm. 
Import the sha224() function from hashlib, 
and extend the user interface to allow that function to be called.

"""

# FIXME: Import sha224 also
from hashlib import md5, sha1, sha224

text = input("Enter text to hash ('q' to quit): ")

algorithm = input('\nEnter algorithm (md5/sha1): ')
if algorithm == 'md5':
    output = md5(text.encode('utf-8'))
elif algorithm == 'sha1':
    output = sha1(text.encode('utf-8'))
elif algorithm == 'sha224':
    output = sha224(text.encode('utf-8'))
else:
    output = 'Invalid algorithm selection'

print('\nHash value:', output.hexdigest())