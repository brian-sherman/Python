"""
String...
1. String Example:

    A.  Write a function that takes a string as an argument and returns a new string consisting of every fourth
        character in the argument.

    B.  Write a function that captures a list of strings, iterates through it, and returns a new string
        consisting of the last character in the string in the list.

An example input:  abcdefgh
Expected Output:
    Problem A:
        dg
An example input: abc def rgi
    Problem B:
        cfi

"""



"""
2. String Slicing Example: str[start : end : stride]    

Complete this function which takes a string as input and return the first 40 characters of the original string
and "..." if the string is more than 45 characters long.  Otherwise, this function returns the original string.

Example Long String:
    Here at WGU, we believe that talent is universal—even if opportunity isn’t. Higher education is the
    best way to bridge that gap, but traditional higher ed wasn't built for the realities facing many of today’s
    students. So we created a university focused on expanding access to education around the country. "

Example Short String:
    WGU exists to change lives

Expected Output:
    Here at WGU, we believe that talent is u...
    WGU exists to change lives

"""


"""
3.  Using Stride Example:

A string slice can take a third index that specifies the “step size;” which is the number of spaces between 
successive characters. A step size of 2 means every other character; 3 means every third, and so on.

For example:
    fruit ='banana'
    fruit[0:5:2] # syntax: string[start:end:step]
    Output:  'bnn'

In addition, a step size of -1 goes through the word backwards, so the slice[::-1] generates a reversed string.  

Create a function to ask a user to type in a string and check if the string is a palindrome.

Expected Output:
    Enter a String:  racecar
    racecar, is a palindrome
    
    Enter a String: Hello
    Hello, is not a palindrome

"""


"""
4. Printing Examples:

Practice the different types of print for strings, tuples, lists, dictionaries.  Do you get the same output?

"""


"""
5.  Set Precision Example:

Create a function that asks the user for a floating point number and format the number to 2 decimal places.
Print the result using the 3 methods below.

Expected Output:
    Enter the floating point value: 3.45675
    Formatting the number 3.45675 to 2 decimal places is 3.46

There are 3 ways to set precision of floating point values:
    You can use the % operator.  
    You can use the format() function. 
    You can use the round(x, n) function which takes 2 arguments.
    
"""




"""
6.  String Method Examples:

    A.  Create a function that takes in a string as input and replaces a word with another word.

Hint:  Use the find method to search for the string, and replace method to replace the string with the new string.

    B.  Write a function to replace every lowercase word to upper case equivalent.
    C.  Write a function to replace a string with its acronyms

"""




"""
7.  List Method Example:

Create a function that count the number of word repetition in a string.

Hint:  Use the split method to split the words and put in a list the repetitive word.  The length of the list
will give you the number of occurrences.

"""








"""
8.  Enumerate Example:

Write a program that creates a list of items.  Add an automatic counter that will keep track of the items in your list.
    A. display the result of your items.
    B. change the index number to start at 100 of your list and display the result.

Hint:  Use the built-in enumerate method.

Input:
    apple
    banana
    grapes

Expected Output:
    0 apple
    1 banana
    2 grapes

"""



"""
9.  List Comprehension Example:

Create a program that takes a list of numbers as input and returns a list of each number times 3 using 
list comprehension.

"""



"""
10.  Nested Dictionaries Example:

The following program uses nested dictionaries to display the following:
    "George is on guitar1 in The Beatles."
    
Dictionary:
    bands = {
      "Beatles": {
        "guitar1":"George", "guitar2": "John", "bass": "Paul", "drums": "Ringo"
        },
      "Stones": {
        "vocals": "Mick", "guitar1":"Keith", "guitar2": "Ronnie", "bass": "Darryl", "drums": "Charlie"
        },
      "Heartbreakers": {
        "vocals": "Tom", "guitar1":"Mike", "guitar2": "Tom", "bass": "Ron", "drums": "Steve",
          "keyboards": "Ben", "everything": "Scott"
        }
    }
 
"""
