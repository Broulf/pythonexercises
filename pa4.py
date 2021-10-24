# Author:          Anthony Segura
# ULID:            C00441031
# Course/Section:  CMPS 150 – 002
# Assignment:      pa4 
# Date Assigned:   Sunday, October 17, 2021 
# Date/Time Due:   Saturday, October 23, 2021 –- 11:59 pm 
# 
# Description:     This program calculates the number of trick-or-treaters that visit a 
#    house and the number and types of treat_amount distributed.  
# 
# Certification of Authenticity: 
# I certify that this assignment is entirely my own work.

import random

print ("  ________     _______     _______")
print (" |        \   /       \   /       \\")
print (" |         \ |         | |         |")
print (" |         / |         | |         |")
print (" |________/  |         | |         |")
print (" |        \  |         | |         |")
print (" |         \ |         | |         |")
print (" |         / |         | |         |")
print (" |________/   \_______/   \_______/")
print ()

treat_amount = random.randint(10, 15)
candy_type = ["Snickers", "Skittles", "Twizzlers"]
treats = [0, 0, 0]
treaters = 0

while treat_amount > 0:
    # Store the amount of treaters, per loop
    treaters = treaters + 1
    print("There are", treat_amount, "candies in the bowl.")
    # RNG for amount of candy wanted
    treat_amount_want = random.randint(1, 3)
    print("The trick-or-treater wants", treat_amount_want)

    if treat_amount >= treat_amount_want:
        print("Yes, you get", treat_amount_want, "treat(s)!")
        # For loop for selecting candy and storing the treats
        for i in range(1, treat_amount_want + 1):
            x = random.randint(1, 3)
            print("   Candy", i, ":", candy_type[x-1])
            treats[x-1] = treats[x-1] + 1
        treat_amount = treat_amount - treat_amount_want

    else:
        print("Yes, you get", treat_amount, "treat(s)!")
        # For loop for selecting candy and storing the treats
        for i in range(1, treat_amount + 1):
            x = random.randint(1, 3)
            print("   Candy", i, ":", candy_type[x-1])
            treats[x-1] = treats[x-1] + 1
        treat_amount = 0
    print()

print("*" * 46)
print("The candy is all gone!")
print("There were", treaters, "trick-or-treaters.")
print("You gave out:")
#debug line for treat storage
#print(treats)
print("   ", treats[0], "Snickers")
print("   ", treats[1], "Skittles")
print("   ", treats[2], "Twizzlers\n")
