"""
Complete the program to print out nicely formatted football player statistics. 
Match the following output as closely as possible -- 
the ordering of players is not important for this example.

2012 quarterback statistics:
  Passes completed:
    Greg McElroy   :  19
    Aaron Rodgers  : 371
    Peyton Manning : 400
    Matt Leinart   :  16
  Passing yards:
    ...
  Touchdowns / Interception ratio:
    Greg McElroy   : 1.00
    Aaron Rodgers  : 4.88
    Peyton Manning : 3.36
    Matt Leinart   : 0.00

"""

quarterback_stats = {
    'Aaron Rodgers': {'COMP': 371, 'YDS': 4925, 'TD': 39, 'INT': 8},
    'Peyton Manning': {'COMP': 400, 'YDS': 4659, 'TD': 37, 'INT': 11},
    'Greg McElroy': {'COMP': 19, 'YDS': 214, 'TD': 1, 'INT': 1},
    'Matt Leinart': {'COMP': 16, 'YDS': 115, 'TD': 0, 'INT': 1}
}

print('2012 quarterback statistics:')

print('  Passes completed:')
for qb in quarterback_stats:
    comp = quarterback_stats[qb]['COMP']
    print('    %-s: %d' % (qb, comp))  

print('  Passing yards:')
for qb in quarterback_stats:
    print('    QB: yards')

print('  Touchdown / interception ratio:')
for qb in quarterback_stats:
    ratio = quarterback_stats[qb]['TD'] / quarterback_stats[qb]['INT']
    print('    %-s: %.2f' % (qb, ratio))
