"""
8.  Tuple Example:

Read a tuple from user as input and print another tuple with the first and last item,
and your name in the middle.

For example, if the input tuple is ("this", "is", "input", "tuple"), the return value should be 
("this", "Rabor", "tuple")

Example One:
Enter your name to append into the tuple: Rabor
Expected Result:  ('this', 'Rabor', 'tuple')

"""
string = input("Enter a tuple seperated by spaces: ")
name = input("Enter your name: ")
list = string.split()

new_t = (list[0], name, list[-1])

print(new_t)