# I will keep one variable for original and final amount
# to keep the code simple.

vat = 25.5
price = float(input("Give price without VAT:\n"))

price = price + (price * (vat / 100))

print(f"Price with VAT: {price}€")