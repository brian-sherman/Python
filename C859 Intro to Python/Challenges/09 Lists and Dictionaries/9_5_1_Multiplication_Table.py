"""
Print the two-dimensional list mult_table by row and column. 
Hint: Use nested loops. 

Sample output for the given program:
1 | 2 | 3
2 | 4 | 6
3 | 6 | 9

"""

mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

for row in mult_table:
    for element in row:
        list_len = len(row)
        current_idx = row.index(element)
        list_end = list_len - current_idx
        if list_end != 1:
            next_idx = current_idx + 1
            print(element, end=' | ')
        else:
            print(element, end='')
    print()