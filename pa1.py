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

# Asks the user for needed inputs
make_model = input("Enter the make and model of the vehicle: ")
tire_diameter = eval(input("Enter the tire diameter (inches): "))
distance_traveled = eval(input("Enter the distance traveled (miles): "))
average_speed = eval(input("Enter the average driving speed in mph: "))

# Calculations for all needed values
tire_circumfrence = tire_diameter * 3.1416
distance_traveled_inches = distance_traveled * 5280 * 12
tire_rotations_exact = distance_traveled_inches / tire_circumfrence
tire_rotations_approx = distance_traveled_inches // tire_circumfrence
travel_hours = format(distance_traveled / average_speed , ".3f")

# Shows the Summary
print("\nSummary of travel information for", make_model, ":")
print(49 * "-")
print("Tire size:", tire_diameter, "inches")
print("Tire circumfrence:", tire_circumfrence, "inches")
print("Distance traveled:", distance_traveled, "miles", "(", distance_traveled_inches, "inches", ")")
print("Speed traveled: ", average_speed, "mph")

# Shows the Tire Rotation information
print("\nNumber of Tire Rotations:")
print(49 * "-")
print("\tExact:", tire_rotations_exact)
print("\tApprox:", tire_rotations_approx)
print("\nIt will take", travel_hours, "hours to travel", distance_traveled, "miles")
