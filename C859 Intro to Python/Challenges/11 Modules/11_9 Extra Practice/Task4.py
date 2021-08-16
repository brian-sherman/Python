"""
Complete the function to return the current date

import datetime as dt

def currentDate():
# Student code goes here
 
print(currentDate()) #Expected outcome will vary, but should follow this format: The current date is 9-11-2018.

"""

import datetime as dt

def currentDate():
    today = dt.date.today()
    return today
 
print(currentDate()) #Expected outcome will vary, but should follow this format: The current date is 9-11-2018.