# Author:         Anthony Segura
# ULID/Section:   C00441031 / CMPS150-002
# Lab #4 

# Ask the user for a number
print()
num = eval(input("Enter a number: "))

# Determine if the input number is positive, negative or zero
if num < 0:
    print("You entered a negative number!")
elif num == 0:
    print("You entered zero!")
elif num > 0:
    print("You entered a positive number!")

# Ask the user for how many years they have worked for a company
print()
years = eval(input("Enter years worked: "))

# Respond with raise category
if years < 5:
    print("Raise category = 3 %")
else:
    print("Raise category = 5 %\n")
