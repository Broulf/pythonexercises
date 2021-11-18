# Author:         Anthony Segura
# ULID/Section:   C00441031 CMPS150-002
# Lab #6

# Part I
# print a blank line
print()

# pounds/kilograms table
print(" Pounds     Kilograms")
print("---------------------")

pounds = 1
kilograms = .453592 * pounds

count = 10
while count <= 100:
    print("  ", count, "\t     ", round(count * kilograms, 2))
    count = count + 10

# Part II
# print 2 blank lines using \n escape sequence
print("\n")

# inches/centimeters table
print(" Inches  Centimeters")
print("--------------------")

inches = 1
centimeters = inches * 2.54

count = 18.50
while count >= 6.50:
    print(" ", count, "\t   ", round(count * centimeters, 2))
    count = count - 1.5 

print("\n")
