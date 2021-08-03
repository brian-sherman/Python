"""
Assign sum_extra with the total extra credit received given list test_grades. 
Full credit is 100, so anything over 100 is extra credit. 
For the given program, sum_extra is 8 because 1 + 0 + 7 + 0 is 8. 
Sample output for the given program:
Sum extra: 8

"""

test_grades = [101, 83, 107, 90]
sum_extra = -999 # Initialize 0 before your loop

sum_extra = 0 
for i in test_grades:
    if i > 100:
        extra = i - 100
        sum_extra += extra

print('Sum extra:', sum_extra)