"""
Write a program that lets a user enter N and that outputs N! (N factorial, meaning N*(N-1)*(N-2)*...*2*1). 
Hint: Initialize a variable total to N (where N is input), and use a loop variable i that counts from total-1 down to 1. 
Compare your output with some of these answers: 1:1, 2:2, 3:6, 4:24, 5:120, 8:40320.
"""

N = int(input())  # Read user-entered number
total = N
i = total

while i >= 2:
    # Decrement i
    i = i - 1
    # Set total to total * (i)
    total = total * i

print(total)