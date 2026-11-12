# variable to store the biggest number
biggest = 0

# iteration that runs 5 times
for iteration in range(5):
    number = input("Give a number:\n")
    number = int(number)

    #this breaks the iteration
    # and gives the given biggest number till now
    if number < 0:
        break
    # this is the actual part that checks the biggest number
    if number > biggest:
        biggest = number

# printing the biggest number
print(f"The biggest number from user: {biggest}")


# no AI has been used in writing this code