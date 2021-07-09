"""
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) and the user must repeat the sequence. Create a for loop that compares the two strings. For each match, add one point to user_score. Upon a mismatch, end the game. Ex: The following patterns yield a user_score of 4:

simonPattern: R, R, G, B, R, Y, Y, B, G, Y
userPattern:  R, R, G, B, B, R, Y, B, G, Y
"""


user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern  = 'RRGBBRYBGY'

for i in range(len(simon_pattern)):
    if user_pattern[i] == simon_pattern[i]:
        user_score += 1
    else:
        break

print('User score:', user_score)