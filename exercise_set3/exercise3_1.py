# taking input from the user for two integers.

first_number = int(input("Give first number: \n"))
second_number = int(input("Give second number: \n"))


# comparing two numbers traditionally...
if first_number > second_number:
    print(f"Bigger number: {first_number}")
elif first_number < second_number:
    print(f"Bigger number: {second_number}")
else:
    print("Numbers are equal.")