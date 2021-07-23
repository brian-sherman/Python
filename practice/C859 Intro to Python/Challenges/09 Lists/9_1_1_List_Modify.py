"""
Modify short_names by deleting the first element and changing the last element to Joe. 
Sample output from given program:
['Sam', 'Ann', 'Joe']

"""

short_names = ['Gertrude', 'Sam', 'Ann', 'Joseph']

del short_names[0]
short_names[-1] = 'Joe'

print(short_names)