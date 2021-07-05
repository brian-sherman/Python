"""
2.  Basic Arithmetic Example:

Write a simple calculator program that prints the following menu: 

1. Addition 
2. Subtraction 
3. Multiplication 
4. Division 
5. Quit 

The user selects the number of the desired operation from the menu.  Prompt the user to enter two numbers and 
return the calculation result.

Example One:
Please select operation -
      1.  Add
      2.  Subtract
      3.  Multiply
      4.  Divide
      5.  Exit
      
Select 1, 2, 3, 4, or 5: 1
Enter the first number: 4
Enter the second number: 5

The Sum of 4 and 5 is: 9

Example Two:
Please select operation -
      1.  Add
      2.  Subtract
      3.  Multiply
      4.  Divide
      5.  Exit
      
Select 1, 2, 3, 4, or 5: 5
GoodBye

"""
while True:
    print("Please select operation -")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    selection = input("Select 1, 2, 3, 4, or 5: ")
    if selection == '5':
        print("GoodBye")
        break
    elif selection == '1' or selection == '2' or selection == '3' or selection == '4':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))  
        if selection == '1': 
            sum = num1 + num2 
            print("The Sum of %d and %d is: %d" % (num1, num2, sum))
        elif selection == '2':
            difference = num1 - num2 
            print("The difference of %d and %d is: %d" % (num1, num2, difference))
        elif selection == '3':
            product = num1 * num2 
            print("The product of %d and %d is: %d" % (num1, num2, product))
        elif selection == '4':
            quotient = num1 / num2 
            print("The product of %d and %d is: %d" % (num1, num2, quotient))
    else:
        print("Sorry I didn't understand that. Please select an option from the menu.")
