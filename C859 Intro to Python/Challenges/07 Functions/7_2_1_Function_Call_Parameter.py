"""
Define a function print_total_inches, 
with parameters num_feet and num_inches, 
that prints the total number of inches. 

Note: There are 12 inches in a foot. 

Ex: print_total_inches(5, 8) prints:

Total inches: 68
"""

def print_total_inches(num_feet, num_inches):
    print("Total inches:", (num_feet * 12) + num_inches)
    
print_total_inches(5, 8)