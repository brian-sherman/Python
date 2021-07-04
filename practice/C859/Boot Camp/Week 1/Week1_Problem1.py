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

