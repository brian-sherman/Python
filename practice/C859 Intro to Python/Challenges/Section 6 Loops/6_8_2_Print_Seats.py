"""
Given num_rows and num_cols, print a list of all seats in a theater. 
Rows are numbered, columns lettered, as in 1A or 3E. 
Print a space after each seat, including after the last. 
Ex: num_rows = 2 and num_cols = 3 prints:
1A 1B 1C 2A 2B 2C 
"""

num_rows = 2
num_cols = 3

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

row = '1'
column = 'A'

for r in range(num_rows): 
   column = 'A' 
   for c in range(num_cols):
      print('%s%s' % (row, column), end=' ') 
      column = chr(ord(column) + 1) 
   row = chr(ord(row) + 1) 

print()