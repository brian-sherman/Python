"""
Complete the function to print the full name of the month using the calendar library

import calendar

# Complete the function to print the full name of the month using the calendar library 
def printMonthName(monthNum):
# Student code goes here
 
# expected output: March
printMonthName(3)
 
# expected output: November
printMonthName(11)

"""

import calendar

# Complete the function to print the full name of the month using the calendar library 
def printMonthName(monthNum):
    name = calendar.month_name[monthNum]
    print(name)
 
# expected output: March
printMonthName(3)
 
# expected output: November
printMonthName(11)