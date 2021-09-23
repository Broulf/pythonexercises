# Author:          Anthony Segura
# ULID:            C00441031
# Course/Section:  CMPS 150 – 002
# Assignment:      pa2
# Date Assigned:   Friday, September 17, 2021
# Date/Time Due:   Thursday, September 23, 2021 –- 11:55 pm
#
# Description:     This program calculates the number of plants that can be placed
#                  in a given space using both a rectangular and triangular pattern
#                  for placement. It uses basic numeric operators as well as the
#                  math library. Finally, it displays formatted output.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.
import math as m

area_length = eval(input("Enter the length of the planting area: "))
area_width = eval(input("Enter the width of the planting area: "))
plant_spacing = eval(input("Enter the spacing between plants: "))

# Ractangular Calulations
number_rows = area_length // plant_spacing
number_columns = area_width // plant_spacing
total_plants_rectangular = number_rows * number_columns

# Rectangular Print
print("\nPlants in a Rectangular Grid")
print("*" * 28)
print("Num of rows:", format(number_rows, '>8'))
print("Num of columns:", format(number_columns, '>5'))
print("Total Plants:", format(total_plants_rectangular, '>7'))

# Triangular Calculations
row_spacing = plant_spacing * .866
number_plants_odd = area_length // plant_spacing
number_plants_even = (area_length - plant_spacing * 0.5) // plant_spacing
total_rows = ((area_width - plant_spacing) // row_spacing) + 1
number_even_rows = total_rows // 2
number_odd_rows = total_rows - number_even_rows
total_plants_triangular = (number_plants_odd * number_odd_rows) + (number_plants_even * number_even_rows)

# Triangular
print("\nPlants in a Triangular Grid")
print("*" * 27)
print("Space between rows:", format(row_spacing, '.3f'))
print("Odd Rows:", "\n   Num of rows:", format(number_odd_rows, '>5'), "\n   Num of plants:", format(number_plants_odd, '>3'))
print("Even Rows:", "\n   Num of rows:", format(number_even_rows, '>5'), "\n   Num of plants: ", format(number_plants_even, '.0f'))
print("\nTotal number of rows:", format(total_rows, '>6'))
print("Total number of plants: ", format(total_plants_triangular, '.0f'), "\n\n")
