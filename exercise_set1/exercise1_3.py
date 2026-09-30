# milage: 6.5 ltr/100km
# have to find the fuel consumed in the trip
milage = 6.5/100

trip_length = int(input("Give the trip length:\n"))

fuel_consumption = trip_length * milage

print(f"Consumption: {fuel_consumption} l")