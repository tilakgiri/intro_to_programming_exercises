# asking user for the temperature

temperature = int(input("Give the temperature:\n"))


# using conditional statement to check the range
if 0 <= temperature <= 10:
    print("COLD")

elif 11 <= temperature <= 15:
    print("CHILLY")

elif 16 <= temperature <= 20:
    print("NORMAL TEMPERATURE")

elif 21 <= temperature <= 25:
    print("WARM")

elif 26 <= temperature <= 30:
    print("HOT")

else:
    print("Try Again :(")