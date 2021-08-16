"""
Run the following program that prints out the response of help(ticket_price). 
Add an additional parameter "vegetarian=False" to ticket_price, 
augment the docstring appropriately, 
and run the program again.

"""


def ticket_price(origin, destination, coach=True, first_class=False, vegetarian=False):
    """Calculates the price of a ticket between two airports.
    Only one of coach or first_class must be True.

    Arguments:
    origin -- string representing code of origin airport
    destination -- string representing code of destination airport

    Optional keyword arguments:
    coach -- Boolean. True if ticket cost priced for a coach class ticket (default True)
    first_class -- Boolean. True if ticket cost priced for a first class ticket (default False)
    vegetarian -- Boolean. True if passanger requires vegetarian meal option (default False)

    """
    #Function body statements ...

help(ticket_price)