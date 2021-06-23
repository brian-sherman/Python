-------------------------------------------------------
#5.2 If-Else Practice

#1)
if user_age > 62:  
	item_discount = 15
else:
	item_discount = 0

#2)
if num_people > 10:
	group_size = 2 * group_size
else:
	group_size = 3 * group_size
	num_people = num_people - 1

#3)
if num_players > 11:
	team_size = 11
else:
	team_size = num_players
team_size = 2 * team_size

#Challenge Activity 1
user_age = 17
if user_age <= 18:
   print('18 or less')
else:
   print('Over 18')

#Challenge Activity 2
user_tickets = 0

if user_tickets < 5:
	num_tickets = 1
else: 
	num_tickets = user_tickets

#Challenge Activity 3
year = 1776

if year >= 2101:
	print('Distant future')
elif year >= 2001:
	print('21st century')
elif year >= 1901:
	print('20th century')
else:
	print('Long ago')
-------------------------------------------------------
#5.3 More if-else

#Challenge Activity 1
car_year = 1964

if car_year <= 1969:
	print('Few safety features.')
if car_year >= 1970:
	print('Probably has seat belts.')
if car_year >= 1990:
	print('Probably has antilock brakes.')
if car_year >= 2000:
	print('Probably has airbags.')
-------------------------------------------------------
#5.4 Equality and relational operators 

#Challenge Activity 1
user_num = int(input('Enter a number: '))

if user_num >= 0:
    print('Non-negative')
else:
    print('Negative')

#Challenge Activity 2
num_cents = 109
if num_cents >= 100:
    print('Dollar or more')
else:
    print('not a dollar')

#Challenge Activity 3
user_grade = 10
if 9 <= user_grade <= 12:
    print('in high school')
else:
    print('not in high school')
-------------------------------------------------------
#5.5 Boolean Operators 

#5)
if (wage > 10) or (age < 18):

#Challenge Activity 1 
special_num = 17

if (special_num == -99) or (special_num == 0) or (special_num == 44):
    print('Special number')
else:
    print('Not special number')

#Challenge Activity 2
user_age = 17

if (user_age > 17) and (user_age != 25):
    print('Eligible')
else:
    print('Ineligible')

#Challenge Activity 3
young = True
famous = False

if (young == True) and (famous == True):
    print('You must be rich!')
else:
    print('There is always the lottery...')
-------------------------------------------------------
#5.6 Membership and identity operators 

#Challenge Activity 
special_list = [-99, 0, 44]
special_num = 17

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')
-------------------------------------------------------
#5.8 Code blocks and indentation 

#Challenge Activity 
if 'New York' in temperatures:
    if temperatures['New York'] > 90:
        print('The city is melting!')
    else:
        print('The temperature in New York is', temperatures['New York'])
else:
    print('The temperature in New York is unknown.')
-------------------------------------------------------
#5.9 Conditional expressions 

#Challenge Activity 1 
user_val = -9

cond_str = 'negative' if (user_val < 0) else 'non-negative'

print(user_val, 'is', cond_str)

#Challenge Activity 2
num_users = 8
update_direction = 3

num_users = (num_users + 1) if (update_direction == 3) else (num_users - 1)

print('New value is:', num_users)
-------------------------------------------------------