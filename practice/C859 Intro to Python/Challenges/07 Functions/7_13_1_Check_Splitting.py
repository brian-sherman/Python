"""
Finish the split_check function. 
The split_check function should return the amount each diner must pay to cover the cost of the meal. 
Use default arguments to set tip_rate to 15% and tax_rate to 9% if the user does not specify them.


def split_check(check_amount, num_diners, tip_rate=0.15, tax_rate = 0.09):
    pass
    # FIXME: Finish the function. HINT: Calculate bill total with tip and tax,
    # then divide by the number of diners.

total = float(input('Enter bill total:\n'))
people = int(input('Enter number of diners:\n'))

print('Cost per diner:', split_check(total, people, tax_rate = 0.075))
"""


def split_check(check_amount, num_diners, tip_rate=0.15, tax_rate = 0.09):
    total = ((check_amount + (check_amount * tip_rate) + (check_amount * tax_rate))) / num_diners
    return total

total = float(input('Enter bill total:\n'))
people = int(input('Enter number of diners:\n'))

print('Cost per diner:', split_check(total, people, tax_rate = 0.075))