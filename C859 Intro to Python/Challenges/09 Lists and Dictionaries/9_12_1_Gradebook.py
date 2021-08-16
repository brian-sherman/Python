"""
Complete the program that implements a gradebook. 
The student_grades dict should consist of entries whose keys are student names, 
and whose values are lists of student scores.

"""

student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        if name in student_grades:
            student_grades[name].append(grade)
        else:
            student_grades.setdefault(name, []).append(grade)
    elif command == '2':
        name, grade = input(grade_prompt).split()
        if name in student_grades:
            student_grades[name].remove(grade)
        else:
            print("That student doesn't exist")
    elif command == '3':
        print(student_grades)
    elif command == '4':
        break
    else:
        print('Unrecognized command.')