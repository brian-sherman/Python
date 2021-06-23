while True:
    try:
        starting_balance = float(input("What is your starting balance? "))
    except ValueError:
        print("Sorry, I didn't understand that. Please enter a number.")
    else:
        break
while True:
    try:
        monthly_contribution = float(input("How much will you be contributing monthly? "))
    except ValueError:
        print("Sorry, I didn't understand that. Please enter a number.")
    else:
        break
while True:
    try:
        expected_interest = int(input("What is your targeted return percentage? "))
    except ValueError:
        print("Sorry, I didn't understand that. Please enter a number.")
    else:
        expected_interest = expected_interest / 100
        break
while True:
    try:
        time = float(input("How many years will you be investing? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
    else:
        break

compounded_starting_balance = starting_balance * (1 + (expected_interest / 12)) ** (12 * time)
compounded_monthly_contribution = monthly_contribution * (((1 + expected_interest / 12) ** (12 * time) - 1) / (expected_interest / 12)) * (1 + expected_interest / 12)
future_balance = compounded_starting_balance + compounded_monthly_contribution

print("Your expected future balance is $%f" % future_balance)

input("Press Enter to exit...")


