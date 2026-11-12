# creating a tuple
months = ("January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December")

# taking month number and correcting the index issue
month_num = input("Give the number of month:\n")
month_num = int(month_num) - 1

# here i have not created else condition for mistake
# because of recommended line of code expected in the exercise
result = months[month_num]
print(result)


# no AI has been used to write this code