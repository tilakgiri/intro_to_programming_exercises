import math
# asking user for the value of a & b leg

a_leg = float(input("Give the first leg:\n"))
b_leg = float(input("Give the second leg:\n"))

hypotenuse = math.sqrt(math.pow(a_leg, 2) + math.pow(b_leg, 2))

hypotenuse = round(hypotenuse, 1)

print(f"Hypotenuse: {hypotenuse} m")