final_value = eval(input("Enter final account value: "))
annual_rate = eval(input("Enter annual interest rate in percent: "))
monthly_rate = annual_rate / 12
years = eval(input("Enter number of years: "))
months = years / 12

initial_deposit = (final_value) / ((1 + monthly_rate) ** months)

print("Initial deposit value is", initial_deposit)
