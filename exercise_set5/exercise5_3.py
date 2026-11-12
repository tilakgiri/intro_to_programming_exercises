# using math lib for pow and pi
#using run boolean as a switch
import math
run = True

while run:
    radius = input("Give radius:\n")
    radius = float(radius)

    area = math.pi * math.pow(radius, 2)
    area = round(area, 2)

    print(f"Circle area: {area}")

    decision = input("Do you want to continue? (y/n)\n")
    # here only one if statement is enough
    # since y or wrong input results in repetition of program :)
    if decision == "n":
        run = False


# no AI was used in the writing of this program