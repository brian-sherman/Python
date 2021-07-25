"""
Write a loop to print all elements in hourly_temperature. 
Separate elements with a -> surrounded by spaces. 
Sample output for the given program:

90 -> 92 -> 94 -> 95 
Note: 95 is followed by a space, then a newline.

"""

hourly_temperature = [90, 92, 94, 95]

list_len = len(hourly_temperature)

for t in hourly_temperature:
    current_idx = hourly_temperature.index(t)
    list_end = list_len - current_idx
    if list_end != 1:
        next_idx = current_idx + 1
        print('%d ->' % (t), end=' ')
    else:
        print(t, end=' ')
        print()