"""
Address the FIXME comments. 
Move the respective code from the while-loop to the created function. 
The add_grade function has already been created.

Note: split() and strip() are string methods further explained elsewhere. 
split() separates a string into tokens using any whitespace as the default separator. 
The tokens are returned in a list (i.e., 'a b c'.split() returns ['a', 'b', 'c']). 
strip() returns a copy of a string with leading and trailing whitespace removed.

def add_grade(student_grades):
    print('Entering grade. \n')
    name, grade = input(grade_prompt).split()
    student_grades[name] = grade

# FIXME: Create delete_name function

# FIXME: Create print_grades function

student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
delete_prompt = "Enter name to delete:\n"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n\n")

command = input(menu_prompt).lower().strip()

while command != '4':  # Exit when user enters '4'
    if command == '1':
        add_grade(student_grades)
    elif command == '2':
        # FIXME: Only call delete_name() here
        print('Deleting grade.\n')
        name = input(delete_prompt)
        del student_grades[name]
    elif command == '3':
        # FIXME: Only call print_grades() here
        print('Printing grades.\n')
        for name, grade in student_grades.items():
            print(name, 'has a', grade)
    else:
        print('Unrecognized command.\n')

    command = input().lower().strip()

"""

def add_grade(student_grades):
    print('Entering grade. \n')
    name, grade = input(grade_prompt).split()
    student_grades[name] = grade

# FIXME: Create delete_name function
def delete_name():
    name = input(delete_prompt)
    print('Deleting grade.\n')
    del student_grades[name]

# FIXME: Create print_grades function
def print_grades():
    print('Printing grades.\n')
    for name, grade in student_grades.items():
            print(name, 'has a', grade)

student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
delete_prompt = "Enter name to delete:\n"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n\n")

command = input(menu_prompt).lower().strip()

while command != '4':  # Exit when user enters '4'
    if command == '1':
        add_grade(student_grades)
    elif command == '2':
        delete_name()
    elif command == '3':
       print_grades()
    else:
        print('Unrecognized command.\n')

    command = input().lower().strip()
