# Author: Anthony Segura
# ULID/Section: C00441031 / CMPS150-002 
 
# get user input  
my_city = input("Enter your hometown: ") 
speed = eval(input("Enter the speed of a vehicle in mph: ")) 
hours = eval(input("Enter the hours a vehicle traveled: ")) 
 
# compute distance vehicle traveled 
distance = speed * hours 
 
# print output 
print() 
print("Your hometown is:", my_city) 
print("The vehicle traveled", distance, "miles!")
