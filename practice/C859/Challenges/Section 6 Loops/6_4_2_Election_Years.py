"""
Write a program that prints the U.S. presidential election years from 1792 to present day, knowing that such elections occur every 4 years.

Hint: Initialize your loop variable to 1792. Don't forget to use <= rather than == to help avoid an infinite loop.
"""

year = 1792
current_year = 2021

while year <= current_year:
    print("Election Year =", year)
    year = year + 4