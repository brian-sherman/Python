#Weighted Grades

exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))

prog1_grade = float(input('Enter score on Assignment 1 (out of 50):\n'))
prog2_grade = float(input('Enter score on Assignment 2 (out of 50):\n'))
prog3_grade = float(input('Enter score on Assignment 3 (out of 50):\n'))
prog4_grade = float(input('Enter score on Assignment 4 (out of 50):\n'))

prog1_grade = (prog1_grade / 50) * 100
prog2_grade = (prog2_grade / 50) * 100
prog3_grade = (prog3_grade / 50) * 100
prog4_grade = (prog4_grade / 50) * 100

averageExamScore = ((exam1_grade + exam2_grade + exam3_grade) / 3)
averageProgScore = ((prog1_grade + prog2_grade + prog3_grade + prog4_grade) / 4)

overall_grade = (0.6 * averageExamScore) + (0.4 * averageProgScore)

print('Your overall grade is:', overall_grade)
