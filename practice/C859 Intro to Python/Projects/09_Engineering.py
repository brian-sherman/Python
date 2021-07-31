"""
A list can be useful in solving various engineering problems. 
One problem is computing the voltage drop across a series of resistors. 
If the total voltage across the resistors is V, 
then the current through the resistors will be I = V/R, 
where R is the sum of the resistances. 
The voltage drop Vx across resistor x is then Vx = I · Rx.

zyDE 9.11.1: Calculate voltage drops across series of resistors.
The following program uses a list to store a user-entered set of resistance values and computes I.

Modify the program to compute the voltage drop across each resistor, 
store each in another list voltage_drop, and finally print the results in the following format:

5 resistors are in series.
This program calculates the voltage drop across each resistor.
Input voltage applied to circuit: 12.0
Input ohms of 5 resistors
1) 3.3
2) 1.5
3) 2.0
4) 4.0
5) 2.2
Voltage drop per resistor is
1) 3.0 V
2) 1.4 V
3) 1.8 V
4) 3.7 V
5) 2.0 V

"""

num_resistors = 5
resistors = []
voltage_drop = []

print( '%d resistors are in series.' % num_resistors)
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print (input_voltage)

print('Input ohms of %d resistors' % num_resistors)
for i in range(num_resistors):
    res = float(input('%d)' % (i + 1)))
    print(res)
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)

# Calculate voltage drop over each resistor
# ...

# Print the voltage drop per resistor
# ...

7