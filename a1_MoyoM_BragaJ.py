# PROG1925 Assignment 1 Marianne Moyo and Joey Braga
# Date Created Sept 20th 2024
# Revision History: Last edited Sept 20 2024
from typing import Final

SUBSIDY = 12.85
TAXES = 1.13
Customer_name = str(input("Please enter your name: "))
Customer_id = str(input("Please enter your ID: "))
Electricity_consumed = int(input("Please enter how many units of electricity you used this month: "))
Subsidy_eligible = input("Please enter Yes or No if you are eligible for a subsidy: ")
Customer_Years = int(input("Please enter how many years you have been a customer: "))
Subsidy_total = None
Subsidy_amount= None
Unit_fee = None
Loyalty = float(Customer_Years)

if Electricity_consumed >= 800:
    Unit_fee = Electricity_consumed * 0.75
elif Electricity_consumed >= 500:
    Unit_fee = Electricity_consumed * 0.50
elif Electricity_consumed >= 200:
    Unit_fee = Electricity_consumed * 0.30
else:
    Unit_fee = Electricity_consumed * 0.20

if Subsidy_eligible == "Yes":
    Subsidy_total = Unit_fee * ((100 - SUBSIDY) / 100 )
    Subsidy_amount = Unit_fee - Subsidy_total
else:
    Subsidy_total = 0

match Customer_Years:
    case 0 | 1:
        Loyalty = 0
    case 2 | 3:
        Loyalty = 5
    case 4 | 5 | 6:
        Loyalty = 10
    case 7 | 8 | 9 | 10:
        Loyalty = 15

Subtotal = Unit_fee - (Loyalty + Subsidy_amount)
if Subtotal < 30:
    Subtotal = 30
Subtotal_taxes = (Subtotal * TAXES) - Subtotal

Final_total = Subtotal * TAXES

