"""
The following program calculates the number of times the sum of two dice (randomly rolled) is equal to six or seven.

import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid number of rolls. Try again.')

Create a different version of the program that:

1. Calculates the number of times the sum of the randomly rolled dice equals each possible value from 2 to 12.
2. Repeatedly asks the user for the number of times to roll the dice, quitting only when the user-entered number is less than 1. 
    Hint: Use a while loop that will execute as long as num_rolls is greater than 1.
3. Prints a histogram in which the total number of times the dice rolls equals each possible value is displayed by printing a character, such as *, that number of times. 
    The following provides an example:

Dice roll histogram:

2s:  **
3s:  ****
4s:  ***
5s:  ********
6s:  *************
7s:  *****************
8s:  *************
9s:  *********
10s: **********
11s: *****
12s: **

"""

import random

num_rolls = int(input('Enter number of rolls, or 0 to quit:\n'))

while num_rolls >= 1:
    num_twos = num_threes = num_fours = num_fives = num_sixes = num_sevens = num_eights = num_nines = num_tens = num_elevens = num_twelves = 0
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

        if roll_total == 2:
            num_twos = num_twos + 1
        elif roll_total == 3:
            num_threes = num_threes + 1
        elif roll_total == 4:
            num_fours = num_fours + 1
        elif roll_total == 5:
            num_fives = num_fives + 1
        elif roll_total == 6:
            num_sixes = num_sixes + 1
        elif roll_total == 7:
            num_sevens = num_sevens + 1
        elif roll_total == 8:
            num_eights = num_eights + 1  
        elif roll_total == 9:
            num_nines = num_nines + 1   
        elif roll_total == 10:
            num_tens = num_tens + 1
        elif roll_total == 11:
            num_elevens = num_elevens + 1
        elif roll_total == 12:
            num_twelves = num_twelves + 1
        
    print('\nDice roll histogram:')
    print('2s:', end=' ')
    for i in range(num_twos):
        print('*', end='')
    print('\n3s:', end=' ')
    for i in range(num_threes):
        print('*', end='')
    print('\n4s:', end=' ')
    for i in range(num_fours):
        print('*', end='')
    print('\n5s:', end=' ')
    for i in range(num_fives):
        print('*', end='')
    print('\n6s:', end=' ')
    for i in range(num_sixes):
        print('*', end='')
    print('\n7s:', end=' ')
    for i in range(num_sevens):
        print('*', end='')
    print('\n8s:', end=' ')
    for i in range(num_eights):
        print('*', end='')
    print('\n9s:', end=' ')
    for i in range(num_nines):
        print('*', end='')
    print('\n10s:', end=' ')
    for i in range(num_tens):
        print('*', end='')
    print('\n11s:', end=' ')
    for i in range(num_elevens):
        print('*', end='')
    print('\n12s:', end=' ')
    for i in range(num_twelves):
        print('*', end='')

    num_rolls = int(input('\nEnter number of rolls:\n'))
if num_rolls < 1:
    print("Goodbye")
else:
    print('Invalid number of rolls. Try again.')