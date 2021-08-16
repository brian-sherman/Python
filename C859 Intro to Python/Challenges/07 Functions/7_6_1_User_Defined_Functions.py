"""
The problem below uses the function get_numbers() to read a number of integers from the user. 
Three unfinished functions are defined, which should print only certain types of numbers that the user entered. 
Complete the unfinished functions, adding loops and branches where necessary. 
Match the output with the below sample:

Enter 5 integers:
0 5
1 99
2 -44
3 0
4 12
Numbers: 5 99 -44 0 12
Odd numbers: 5 99
Negative numbers: -44


size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:')

def print_odd_numbers(numbers):
    # Print all odd numbers
    print('Odd numbers:')

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)


"""

size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:', end=" ")
    for i in numbers:
        print(i, end=" ")

def print_odd_numbers(numbers):
    # Print all odd numbers
    odd_numbers = []
    for i in numbers: 
        if (i % 2) != 0:
            odd_numbers.append(i)
    print('\nOdd numbers:', end=" ")
    for i in odd_numbers:
        print(i, end=" ")

def print_negative_numbers(numbers):
    # Print all negative numbers
    neg_numbers = []
    for i in numbers:
        if i < 0:
            neg_numbers.append(i)
    print('\nNegative numbers:', end=" ")
    for i in neg_numbers:
        print(i, end=" ")

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)