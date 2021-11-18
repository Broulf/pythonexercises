# Author:   Anthony Segura
# ULID/Section:   C00441031 / CMPS150-002

# Print 2 blank lines
for i in range(2):
    print()

#print("\n") - Also valid for printing two blank lines

#print() - Another, yet more boring way of printing two lines
#print()

# User inputs hours and the hourly rate
hours_worked = eval(input("Input the amount of hours worked: "))
pay_rate = eval(input("Input the rate of pay per hour: "))

# Calculates the gross pay based on the amount of hours worked an the rate of pay per hour
pay_gross = hours_worked * pay_rate

# Print 1 blank line
print()

# Print out hours, rate and gross pay that you just computed
print("Hours =", hours_worked)
print("Rate =", pay_rate)
print("Gross Pay =", pay_gross)
