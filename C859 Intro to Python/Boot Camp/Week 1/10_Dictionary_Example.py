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
characters = {"Gilligan":"First Mate","Skipper":"Captain","Professor":"Scientist","Mary Ann":"Farm Girl","Ginger":"Movie Star","Thurston":"Rich Guy","Lovey":"Wife"}

set = set()

for key,value in characters.items():
    set.add(key + " : " + value)

print(set)