"""
Write a function number_of_pennies() that returns the total number of pennies 
given a number of dollars and (optionally) a number of pennies. 

Ex: 5 dollars and 6 pennies returns 506.
''' Your solution goes here '''

print(number_of_pennies(5, 6)) # Should print 506
print(number_of_pennies(4))    # Should print 400
"""

def number_of_pennies(dollars=0, pennies=0):
    total_pennies = dollars * 100 + pennies
    return total_pennies

print(number_of_pennies(5, 6)) # Should print 506
print(number_of_pennies(4))    # Should print 400