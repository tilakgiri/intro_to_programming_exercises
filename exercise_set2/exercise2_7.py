import math

value_a = int(input("Entet the value of a: \n"))
value_b = int(input("Enter the value of b: \n"))
value_c = int(input("Enter the value of c: \n"))


# im getting a math domain error
# i think its beacuse the value of b^2 - 4ac is negative
first_x = (0 - value_b + math.sqrt((value_b ** 2) - (4 * value_a * value_c))) / (2 * value_a)

second_x = (0 - value_b - math.sqrt((value_b ** 2) - (4 * value_a * value_c))) / (2 * value_a)

print(f"First value of x: {first_x}")
print(f"Second value of x: {second_x}")