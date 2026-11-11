# taking the necessary inputs from the user
working_hours = int(input("How many workhours this week?\n"))
hourly_wage = int(input("Your hourly salary?\n"))


# using conditional statement to check which case applies for the given input
if working_hours > 40:
    # separating regular hours from the overtime hours
    overtime_hours = working_hours - 40
    regular_hours = 40
    overtime_wage = hourly_wage * 1.5
    weekly_wage = (regular_hours * hourly_wage) + (overtime_hours * overtime_wage)
else:
    # condition for when there is not overtime
    weekly_wage = working_hours * hourly_wage

print(f"Your weekly wage is: {weekly_wage}€")