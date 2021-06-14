"""
Variables:
  myString
  list1
  name
  first_name

Assignments:
  num = 1
  result = num + 8

Equality:
  a == b

"""

"""
1.  String Example:

Read a string from a user and display a string made of the first 2 and last 2 characters of the original string,
so if the user types 'snowflake', the expected result would be 'snke'. It prints the first 2 characters and
combines it with the last 2 characters in the inputted string.  Now what if the user types in 1 characters?
like ‘a’, if the string length is less than 2, then let us display a message saying, “Not enough characters,
please enter a word greater than 2 characters.

Please see the examples below:

Example one:
Enter a string: snowflake
Expected Output:  snke

Example two:
Enter a string: Welcome to Python
Expected Output:  Weon

Example three:
EEnter a string: a
Expected Output:  Not enough characters, please enter a word greater than 2 characters.

s n o w f l a k e
0 1 2 3 4 5 6 7 8
              -2  -1
-1 0 1 2 3 4 5 6 7 8
"""

user_str = input("Enter a string: ")
if len(user_str) >= 2:
    print((user_str[0:2]) + (user_str[-2:]))
else:
    print("Not enough characters, pleases enter a word greater than 2 characters.")

"""
2.  Basic Arithmetic Example:

Write a simple calculator program that prints the following menu: 

1. Addition 
2. Subtraction 
3. Multiplication 
4. Division 
5. Quit 

The user selects the number of the desired operation from the menu.  Prompt the user to enter two numbers and 
return the calculation result.

Example One:
Please select operation -
      1.  Add
      2.  Subtract
      3.  Multiply
      4.  Divide
      5.  Exit
      
Select 1, 2, 3, 4, or 5: 1
Enter the first number: 4
Enter the second number: 5

The Sum of 4 and 5 is: 9

Example Two:
Please select operation -
      1.  Add
      2.  Subtract
      3.  Multiply
      4.  Divide
      5.  Exit
      
Select 1, 2, 3, 4, or 5: 5
GoodBye

"""




"""
3.  Arithmetic Example2 (Convert Seconds):

Write a program to convert Seconds into Hours, Minutes and Seconds.  You should obtain the number of 
seconds as user input (Integer Value).  Convert the seconds into Hours, Minutes, and Seconds, and Display 
that to the User.

Example One:
Enter a number of seconds: 456
Here is the time in hours, minutes, and seconds:
Hours: 0
Minutes: 7
Seconds: 36

"""




"""
4.  Rounding Example:

Write a program that rounds a number to the thousands position.  For each value read by the user, 
your program should print the original value and the number rounded to the nearest thousands.

Example One:
Enter a Number to round:  2.34567
original value: 2.34567
rounded number: 2.346

"""


"""
Rounding Rules:

1.  floor always rounds towards zero for positive numbers, but away from zero for negative numbers. 
    3.1 therefore rounds to 3 using floor, but -3.1 rounds to -4.
2.  ceil is the opposite of floor, and ceil always rounds away from zero for positive numbers, but 
    towards zero for negative numbers.
3.  round implements a type of rounding called bankers' rounding. In bankers' rounding, we round 
    towards the closest significant figure, except in the case of a tie. In the event of a tie, 
    we round towards the closest even significant figure. So 3.5 rounds to 4, but 2.5 rounds to 2.  

    -9  -8  -7  -6  -5  -4  -3  -2  -1  0  1  2  3  4  5  6  7  8  9
    
"""



"""
Strings Example

Example:
   alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""

"""
Collection Types:

•	List is a collection which is ordered and changeable. Allows duplicate members.
•	Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
•	Set is a collection which is unordered and unindexed. No duplicate members.
•	Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

"""

"""
5.  List Example

Create a program to multiply all the numbers in a list

Example One:
The product of the list is: 720

"""




"""
6.  List Example (Triple Items in a List):

Create a program that takes a list of numbers as input and returns a list of each number times 3.

Example One:
The original list is : [1, 6, 9, 3, 4]
The List tripled is : [3, 18, 27, 9, 12]

"""




"""
7.  Remove square bracket of a list

"""




"""
8.  Tuple Example:

Read a tuple from user as input and print another tuple with the first and last item,
and your name in the middle.

For example, if the input tuple is ("this", "is", "input", "tuple"), the return value should be 
("this", "Rabor", "tuple")

Example One:
Enter your name to append into the tuple: Rabor
Expected Result:  ('this', 'Rabor', 'tuple')

"""




"""
9.  Set Example:

Create a set that removes duplicate values

Example One:
Original List: [1, 3, 4, 4, 5, 3, 7]
My New List is: [1, 3, 4, 5, 7]

"""

"""
9a.  More Set Examples:

Create a program that uses a set to add values to it.

Example One:
["dog", "lion", "giraffe"] # Expected Output

"""


"""
10:  Dictionary Example:

Create a program that takes a dictionary as input and return an unordered list with key and value, 
separated by a colon character

Example One:
Gilligan : First Mate
Skipper : Captain
Professor : Scientist
Mary Ann : Farm Girl
Ginger : Movie Star
Thurston : Rich Guy
Lovey : Wife

"""
# castaways = {
#      "Gilligan": "First Mate",
#      "Skipper": "Captain",
#      "Professor": "Scientist",
#      "Mary Ann": "Farm Girl",
#      "Ginger": "Movie Star",
#      "Thurston": "Rich Guy",
#      "Lovey": "Wife"
# }

