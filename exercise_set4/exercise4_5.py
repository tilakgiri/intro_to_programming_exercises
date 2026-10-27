
special_price = False

is_student = input("Are you a student? (y/n):\n")
travel_month = input("Travel month? (1-12)\n")
travel_month = int(travel_month)

if is_student.lower() == "y":
    special_price = True

    if 6 <= travel_month <= 8:
        special_price = False

elif is_student.lower() == "n":
    special_price = False

else:
    print("Invalid input :(")



if special_price:
    print("Special price!")
else:
    print("Normal price.")