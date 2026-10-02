# asking user for the distance covered in both areas.

# consumption outside urban area = 5.1 ltr / 100km
# consumption inside urban area = 7.5 ltr / 100km

# finding per km consumption first
out_urban_perkm = 5.1 / 100
in_urban_perkm = 7.5 / 100

# taking distance input
out_urban_km = int(input("Kilometers outside urban area:\n"))
in_urban_km = int(input("Kilometers within urban area:\n")) 



# # testing the individual consumption values
# print(f"Consumption outside urban area: {out_urban_perkm} ltr/km")
# print(f"Consumption within urban area: {in_urban_perkm} ltr/km")



# finding the total consumption
total_consumption = (out_urban_km * out_urban_perkm) + (in_urban_km * in_urban_perkm)
total_consumption = round(total_consumption, 2)

print(f"Consumption: {total_consumption} ltr")