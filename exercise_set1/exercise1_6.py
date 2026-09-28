# asking input from the user
cents = int(input("How many cents? (1-100):\n"))

# using division basically checks how many times 50 fits in "cents"
cent50 = cents // 50

# this first removes the 50 cents
# and then checks like the line 5 for 20 cents.
cent20 = cents % 50 // 20

# now we just have to keep moving forward with each coin.
cent10 = cents % 50 % 20 // 10

cent5 = cents % 50 % 20 % 10 // 5

cent2 = cents % 50 % 20 % 10 % 5 // 2

cent1 = cents % 50 % 20 % 10 % 5 % 2 // 1

# printing the distribution of coins in the biggest possible coins.
print(f"Amount of 50 cents: {cent50}")
print(f"Amount of 20 cents: {cent20}")
print(f"Amount of 10 cents: {cent10}")
print(f"Amount of 5 cents: {cent5}")
print(f"Amount of 2 cents: {cent2}")
print(f"Amount of 1 cent: {cent1}")