# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
    print("$%.2f" % (rate))
 
# expected output: $34.79
displayHourlyRate(34.789123)    
 
# expected output: $24.12
displayHourlyRate(24.123456)