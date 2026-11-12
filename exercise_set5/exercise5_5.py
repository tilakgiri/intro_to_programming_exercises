# creating a tuple
months = ("January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December")

# taking month number and correcting the index issue
month_num = input("Give the number of month:\n")
month_num = int(month_num) - 1

# here i have created else condition just in case user does some mistake
if 1 <= month_num <=12:
    result = months[month_num]
    print(result)
else:
    print("Wrong input :(")


# no AI has been used to write this code