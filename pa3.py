# Author:          Anthony Segura
# ULID:            C00441031
# Course/Section:  CMPS 150 – 002
# Assignment:      pa3 
# Date Assigned:   Tuesday, September 28, 2021 
# Date/Time Due:   Sunday, October 3, 2021 –- 11:55 pm 
# 
# Description:     This program calculates the total cost for television services  
#                  based on a selected service plan and the number of months of  
#    service.  
# 
# Certification of Authenticity: 
# I certify that this assignment is entirely my own work.

print("\nMENU OF CABLE OPTIONS\n")
print("Connection     Plan        Price/month")
print("-" * 40)
print("               Basic     $ 119 per month")
print("  Fiber        Plus      $ 152 per month")
print("               Elite     $ 182 per month")
print("-" * 40)
print("               Basic     $  99 per month")
print("  Cable        Plus      $ 129 per month")
print("-" * 40)

choice = input("\nDo you want fiber or cable (F/C)? ").lower()
service_months = eval(input("Enter the number of months of service: "))

print("\nThere are three Standard cable plans: Basic, Plus, and Elite.")
plan = input("enter your plan (B/P/E): ").lower()

if choice == "f":
    choice_new = "Fiber"
elif choice == "c":
    choice_new = "Standard"

if plan == "b" and choice == "f":
    plan_new = "Basic"
    cost_month = 119
elif plan == "p" and choice == "f":
    plan_new = "Plus"
    cost_month = 152
elif plan == "e" and choice == "f":
    plan_new = "Elite"
    cost_month = 182

elif plan == "b" and choice == "c":
    plan_new = "Basic"
    cost_month = 99
elif plan == "p" and choice == "c":
    plan_new = "Plus"
    cost_month = 129

cost_total = cost_month * service_months + 50

print("\nSummary of results")
print("-" * 24)
print(" Connection    ", choice_new)
print(" Plan          ", plan_new)
print(" Months        ", service_months)
print(" Cost/Month   $", cost_month)
print(" Installation $ 50")
print(" Total Cost   $", cost_total)
print()
