import random

def pause():
    programPause = input("Press the <ENTER> key to continue...")

while True:
    print('1 = D4')
    print('2 = D6')
    print('3 = D8')
    print('4 = D10')
    print('5 = D12')
    print('6 = D20')
    print('7 = Exit')
    die_type = input("Select an option from the menu above. ")
    if die_type == '7':
        print("Goodbye")
        break
    elif die_type == '1' or die_type == '2' or die_type == '3' or die_type == '4' or die_type == '5' or die_type == '6':
        num_rolls = int(input("How many dice would you like to roll? "))
        if die_type == '1':
            for i in range(num_rolls):
                die1 = random.randint(1,4)
                print('Roll %d is %d' % (i, die1))
            pause()
        elif die_type == '2':
            for i in range(num_rolls):
                die1 = random.randint(1,6)
                print('Roll %d is %d' % (i, die1))
            pause()
        elif die_type == '3':
            for i in range(num_rolls):
                die1 = random.randint(1,8)
                print('Roll %d is %d' % (i, die1))
            pause()
        elif die_type == '4':
            for i in range(num_rolls):
                die1 = random.randint(1,10)
                print('Roll %d is %d' % (i, die1))
            pause()
        elif die_type == '5':
            for i in range(num_rolls):
                die1 = random.randint(1,12)
                print('Roll %d is %d' % (i, die1))
            pause()
        elif die_type == '6':
            for i in range(num_rolls):
                die1 = random.randint(1,20)
                print('Roll %d is %d' % (i, die1))
            pause()
    else:
        print("Sorry, I didn't understand that")