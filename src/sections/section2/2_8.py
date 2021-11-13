water = eval(input("Enter the amount of water in kilograms: "))
temp1 = eval(input("Enter the inital temperature: "))
temp2 = eval(input("Enter the final temperature: "))
energy = water * (temp2 - temp1) * 4184
print("The energy needed is", energy, "joules")
