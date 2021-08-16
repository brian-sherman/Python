"""
Complete the function that takes an integer as input, multiplies by e, and returns result rounded up

from math import e,ceil

def mathCalculation(x):
# Student code goes here
 
#expected outcome: 9
print(mathCalculation(3))    

#expected outcome: 25
print(mathCalculation(9))

"""

from math import e,ceil

def mathCalculation(x):
    y = e * x
    y = ceil(y)
    return y 
 
#expected outcome: 9
print(mathCalculation(3))    

#expected outcome: 25
print(mathCalculation(9))