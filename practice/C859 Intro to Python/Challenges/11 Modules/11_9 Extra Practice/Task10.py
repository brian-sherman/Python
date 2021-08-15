"""
Complete the function to add 90 days to the given date and return the new date

import datetime

# Complete the function to add 90 days to the given date and return the new date
def add90Days(someDate):
# Student code goes here
 
# expected output: 2018-12-30
print(add90Days(datetime.date(2018, 10, 1)))
 
# expected output: 2015-05-12
print(add90Days(datetime.date(2015, 2, 11)))

"""

import datetime

# Complete the function to add 90 days to the given date and return the new date
def add90Days(someDate):
    span = datetime.timedelta(days=90)
    futuredate = someDate + span
    return futuredate
 
# expected output: 2018-12-30
print(add90Days(datetime.date(2018, 10, 1)))
 
# expected output: 2015-05-12
print(add90Days(datetime.date(2015, 2, 11)))