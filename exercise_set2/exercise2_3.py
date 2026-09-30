# import math

# asking user's salary and tax amount

salary = float(input("Your monthly salary:\n"))
tax = float(input("Your tax percentage:\n"))

tax_amount = (tax / 100) * salary
final_salary = salary - tax_amount

# rounding up the tax and salary
tax_amount = round(tax_amount, 2)
final_salary = round(final_salary, 2)


print(f"Earnings: {final_salary} m")
print(f"Taxes: {tax_amount} m")