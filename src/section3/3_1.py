import math

radius = eval(input("Enter the length from the center to a vertex: "))
side = (2 * radius) * math.sin(math.pi / 5)
area = round(((3 * math.sqrt(3)) / 2) * (side ** 2), 2)

print("The area of the Pentagon is:", area)