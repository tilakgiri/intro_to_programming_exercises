# variable to store sum
total = 0

# iteration for the input
for iteration in range(12):
    total += 1

    rain_amount = input("Give rain amount of month:\n")
    rain_amount = int(rain_amount)

    # adding all month's value
    total += rain_amount

# calculating average
average = total / 12
average = round(average, 1)
print(f"The average for rain = {average} mm")