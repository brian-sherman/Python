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

seconds = int(input("Enter a number of seconds: "))
minutes = seconds / 60
hours = minutes / 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

