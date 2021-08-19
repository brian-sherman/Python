"""
6.  List Example (Triple Items in a List):

Create a program that takes a list of numbers as input and returns a list of each number times 3.

Example One:
The original list is : [1, 6, 9, 3, 4]
The List tripled is : [3, 18, 27, 9, 12]

"""

original_list = [1, 6, 9, 3, 4]
new_list = []

for i in original_list:
    new_list.append(i *3)

print("The original list is : ", original_list)
print("The List tripled is : ", new_list)

