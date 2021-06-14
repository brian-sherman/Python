name = input("Enter name: ")

while True:
    try:
        weight = float(input("Enter weight in pounds: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
    else:
        break

while True:
    try:
        height = float(input("Enter height in inches: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
    else:
        break

bmi = (weight / (height ** 2)) * 703
print("BMI = %f" % bmi)

if bmi < 18.5:
    print("%s is underweight." % name)
elif 18.5 <= bmi <= 24.9:
    print("%s is within the healthy range." % name)
elif 25 <= bmi <= 29.9:
    print("%s is overweight." % name)
else:
    print("%s is obese." % name)

input("Press Enter to exit...")
