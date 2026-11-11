# taking the input from user for necessary values
money = input("Give money:\n")
money = int(money)
purchase_cost = input("Purchase cost:\n")
purchase_cost = int(purchase_cost)

# condition for when the cost is less than the money user has
if money < purchase_cost:
    more_money = input("Not enough money, give more:\n")
    more_money = int(more_money)
    money += more_money

    # condition for when there is change to be returned
    if money > purchase_cost:
        change = money - purchase_cost
        print(f"Thank you. Here's the change: {change} €")

    # condition for when user fails to provide enough money
    else:
        print("You don't have enough money.")
    
    
# condition for when there is enough money in the first time and there is change.
else:
    change = money - purchase_cost
    print(f"Thank you. Here's the change: {change} €")

