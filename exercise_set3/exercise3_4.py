money = input("Give money:\n")
money = int(money)

purchase_cost = input("Purchase cost:\n")
purchase_cost = int(purchase_cost)

if money < purchase_cost:
    more_money = input("Not enough money, give more:\n")
    more_money = int(more_money)

    money += more_money
    
    if money > purchase_cost:
        change = money - purchase_cost
        print(f"Thank you. Here's the change: {change} €")

    else:
        print("You don't have enough money.")
    
    

else:
    change = money - purchase_cost
    print(f"Thank you. Here's the change: {change} €")