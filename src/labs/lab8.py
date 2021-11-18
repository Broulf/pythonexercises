# Author:         Anthony Segura
# ULID/Section:   C00441031 - 001
# Lab #8

# works in idle, but not my VSCode or PyCharm
infile = open("fuel.txt","r")

# read initial data
fuel_type = infile.readline().strip()
fuel_amount = eval(infile.readline().strip())

# prices per gallon
regular_unleaded = 2.12
diesel = 2.35
super_unleaded = 2.62
unleaded_plus = 2.36

# prints the header
print("\n    Fuel Type        Gallons     Bill")
print("-------------------------------------")  

while fuel_type != "X" and fuel_amount != 0:

    if(fuel_type == "R"):
        print(format("Regular Unleaded",'20s'),format(fuel_amount,'7.2f'),format(fuel_amount * regular_unleaded,'8.2f'))
    elif(fuel_type == "D"):
        print(format("Diesel",'20s'),format(fuel_amount,'7.2f'),format(fuel_amount * diesel,'8.2f'))
    elif(fuel_type == "S"):
        print(format("Super Unleaded",'20s'),format(fuel_amount,'7.2f'),format(fuel_amount * super_unleaded,'8.2f'))
    elif(fuel_type == "P"):
        print(format("Unleaded Plus",'20s'),format(fuel_amount,'7.2f'),format(fuel_amount * unleaded_plus,'8.2f'))

    fuel_type = infile.readline().strip()
    fuel_amount = eval(infile.readline().strip())

print()
infile.close()
