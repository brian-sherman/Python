#Health data: Age in days

user_age_years = int(input('enter your age in years:\n'))

user_age_days = user_age_years  * 365

user_age_hours = user_age_days * 24

user_age_minutes = user_age_hours * 60

user_age_seconds = user_age_minutes * 60

user_heart_beats = user_age_minutes * 72

user_sneezes = user_age_days * 4

user_calories_burned = user_age_days * 1800

user_sandwiches_consumed = user_calories_burned / 400

print('You are at least %d days old.' % user_age_days)
print('You are at least %d hours old.' % user_age_hours)
print('You are at least %d minutes old.' % user_age_minutes)
print('You are at least %d seconds old.' % user_age_seconds)
print('Your heart has beat %d times.' % user_heart_beats)
print('You have sneezed %d times.' % user_age_seconds)
print('You have burned %d calories.' % user_calories_burned)
print('That is %d turkey sandwiches.' % user_sandwiches_consumed)