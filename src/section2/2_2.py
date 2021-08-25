import math

num1, num2 = eval(input("Enter the radius and the length of a cylinder: "))
area = num1 * num2 * math.pi
volume = num1 * num2
print("The area is", area, "\nThe volume is", volume)