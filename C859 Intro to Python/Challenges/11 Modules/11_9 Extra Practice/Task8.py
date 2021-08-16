"""
Complete the function to print the full name of the day of the week

import calendar, datetime

# Complete the function to print the full name of the day of the week
def printWeekdayName(year, month, day):
# Student code goes here
 
# expected output: Friday    
printWeekdayName(2001, 8, 31)
 
# expected output: Monday
printWeekdayName(2018, 10, 1)

"""

import calendar, datetime

# Complete the function to print the full name of the day of the week
def printWeekdayName(year, month, day):
    day = datetime.date(year, month, day)
    print(day.strftime("%A"))
 
# expected output: Friday    
printWeekdayName(2001, 8, 31)
 
# expected output: Monday
printWeekdayName(2018, 10, 1)