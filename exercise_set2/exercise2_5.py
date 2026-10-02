import random


# first creating all the requried random numbers.
random_number = random.randint(1,10)
first_random = random.randint(2,10)
second_random = random.randint(2,10)


# making the calculation
random_area = first_random * second_random

# printing everything
print(f"Random number: {random_number}")
print(f"First random side: {first_random}")
print(f"Second random side: {second_random}")
print(f"Rectangle area: {random_area}")