# Author:          Anthony Segura
# ULID:            C00441031
# Course/Section:  CMPS 150 – 002
# Assignment:      pa1
# Date Assigned:   Thursday, September 9, 2021
# Date/Time Due:   Tuesday, September 14, 2021 –- 11:55 pm
#
# Description:     This program uses basic numeric operators to calculate the number of
#    times a tire rotates over a given distance. It also computes the
#    travel time for the specified distance. The needed input is provided
#    by the user.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

import math as m

# Asks the user for needed inputs
make_model = input("Enter the make and model of the vehicle: ")
tire_diameter = input(eval("Enter the tire diameter (inches): "))
distance_traveled = input(eval("Enter the distance traveled (miles): "))
average_speed = input(eval("Enter the average driving speed in mph: "))

tire_circumfrence = tire_diameter * m.pi
distance_traveled_inches = distance_traveled * 5280 * 12
tire_rotations = distance_traveled_inches / tire_circumfrence
travel_hours = distance_traveled / average_speed

print("Summary of travel information for", make_model, ":")
print(49 * "-")
print("Tire size:", tire_diameter, "inches")
print("Tire circumfrence:", tire_circumfrence, "inches")
print("Distance traveled:", distance_traveled, "miles", "(", distance_traveled_inches, ")")
print("Speed traveled: ", average_speed, "mph")
