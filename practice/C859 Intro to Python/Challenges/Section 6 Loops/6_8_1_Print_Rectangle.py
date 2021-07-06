"""
Write nested loops to print a rectangle. Sample output for given program:
* * *  
* * *
"""

num_rows = 2
num_cols = 3

for row in range(num_rows):
    print('*', end=' ')
    for column in range(num_cols - 1):
        print('*', end=' ')
    print('')