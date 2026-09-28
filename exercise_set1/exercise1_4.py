# i will first take input from the user

minute = int(input("Give minutes:\n"))

# now i will convert minutes to hours and minutes
hours = minute // 60
remaining_minutes = minute % 60


print(f"{hours}h {remaining_minutes}min")