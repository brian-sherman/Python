"""
4.  Rounding Example:

Write a program that rounds a number to the thousands position.  
For each value read by the user, 
your program should print the original value and the number rounded to the nearest thousands.

Example One:
Enter a Number to round:  2.34567
original value: 2.34567
rounded number: 2.346

"""

import math 

num = float(input("Enter a Number to round: "))

rnum = round(num, 3)

print("original value: ", num)
print("rounded number: ", rnum)
