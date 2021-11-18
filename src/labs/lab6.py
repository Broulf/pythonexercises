# Author:         Caleb Horn  
# ULID/Section:   C00504912 & 002
# Lab #6

# Part I
# print a blank line
print()

# pounds/kilograms table

print(" Pounds     Kilograms")
print("---------------------")

pounds = 10
Kilograms = 0.453592 * pounds

count = 10
while count < 101:
    print(count," ","   ",count * round(Kilograms, 3))
    count = count + 10









# Part II
# print 2 blank lines using \n escape sequence
print("\n\n")

# inches/centimeters table

print(" Inches  Centimeters")
print("--------------------")

inches = 18.5
centimeters = 2.54 

count = 18.50
while count > 6.51:
    print(count," ", "   ",count * centimeters)
    count = count - 1.5 





