"""
Delete Prussia from country_capital. 

Sample output for the given program:
Prussia deleted? Yes.

"""

country_capital = {'Spain': 'Madrid', 'Togo': 'Lome', 'Prussia': 'Konigsberg'}

del country_capital['Prussia']

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')