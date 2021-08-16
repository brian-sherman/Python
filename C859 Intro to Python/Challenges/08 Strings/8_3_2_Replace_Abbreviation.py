"""
Assign decoded_tweet with user_tweet, 
replacing any occurrence of 'TTYL' with 'talk to you later'. 
Sample output from given program:

Gotta go. I will talk to you later.

"""

user_tweet = 'Gotta go. I will TTYL.'

decoded_tweet = user_tweet.replace('TTYL', 'talk to you later')
print(decoded_tweet)