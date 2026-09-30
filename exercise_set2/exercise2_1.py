import math
# asking user for the value of l, b and h

length = float(input("Enter the first side:\n"))
breadth = float(input("Enter the second side:\n"))
height = float(input("Enter the third side:\n"))

box_volume = length * breadth * height

print(f"Box volume: {box_volume} m3")


# ---------------------------------------------- #
# second part of the program for volume of sphere
# ---------------------------------------------- #

# taking the input

radius = float(input("Give the sphere radius:\n"))

sphere_volume = (4/3) * math.pi * math.pow(radius, 3)

sphere_volume = round(sphere_volume, 1)

print(f"Sphere volume: {sphere_volume} m3")