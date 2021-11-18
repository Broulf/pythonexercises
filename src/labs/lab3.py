# lab3.py

# Author:          Anthony Segura
# ULID/Section:    C00441031 / CMPS150-002

print()

# User inputs
pizza_radius = eval(input("Enter the radius of the pizza in inches: "))
pizza_cost = eval(input("Enter the cost of the pizza: "))

# Calculations
pizza_area = (pizza_radius ** 2) * 3.14159
pizza_cost_inches = pizza_cost / pizza_area

# Prints the exact cost per inch then a rounded cost
print("Price per square inch = $", pizza_cost_inches)
print("Price per square inch = $", round(pizza_cost_inches, 2), "(rounded)\n\n")

# Asks for the three letter word
word = input("Enter a 3-letter word: ")

# Breaks the word down into 3-characters and calculates the ASCII Code
chr_1 = ord(word[0])
chr_2 = ord(word[1])
chr_3 = ord(word[2])

# Prints the letter then its ASCII code
print(word[0], "=", chr_1)
print(word[1], "=", chr_2)
print(word[2], "=", chr_3)
print()
