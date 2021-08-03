"""
Write a program that uses the keys(), values(), and/or items() dict methods to find statistics about the student_grades dictionary. 

Find the following:

Print the name and grade percentage of the student with the highest total of points.
Find the average score of each assignment.
Find and apply a curve to each student's total score, such that the best student has 100% of the total points.

"""


# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}
gpas = {}

for student, grades in student_grades.items():
    gpa = sum(grades) / 5
    gpas[student] = gpa

best = 0
for gpa in gpas.values():
    if gpa > best:
        best = gpa

curve = 100 - best

for student, gpa in gpas.items():
    if gpa == best:
        print('The best performing student was %s with a gpa of %d' % (student, gpa))

print()

assignments = []
assignment1 = 0
assignment2 = 0
assignment3 = 0
assignment4 = 0 
assignment5 = 0

for grade in student_grades.values():
    assignment1 += grade[0]
    assignment2 += grade[1]
    assignment3 += grade[2]
    assignment4 += grade[3]
    assignment5 += grade[4]

print('Assignment 1 Average = ', assignment1 / 5)
print('Assignment 2 Average = ', assignment2 / 5)
print('Assignment 3 Average = ', assignment3 / 5)
print('Assignment 4 Average = ', assignment4 / 5)
print('Assignment 5 Average = ', assignment5 / 5)

print()

for student, gpa in gpas.items():
    gpa += curve 
    print('%s\'s curved gpa is %d' % (student, gpa))
