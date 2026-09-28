# Create an application that asks the length of a road trip (kilometers)
# from the user. Calculate the estimated fuel consumption for the trip. 

# milage: 6.5 ltr/100km
milage = 6.5/100

trip_length = int(input("Give the trip length:\n"))

fuel_consumption = trip_length * milage

print(f"Consumption: {fuel_consumption} l")