"""
Complete the if-else statement to print 
'LOL means laughing out loud' 
if user_tweet contains 'LOL'. 
Sample output from given program:

LOL means laughing out loud.
"""

user_tweet = 'I was LOL during the whole movie!'

lol = 'LOL'
if lol in user_tweet:
    print('LOL means laughing out loud.')
else:
    print('No abbreviation.')