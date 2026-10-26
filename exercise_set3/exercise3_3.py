working_hours = int(input("How many workhours this week?\n"))

hourly_wage = int(input("Your hourly salary?\n"))

if working_hours > 40:
    overtime_hours = working_hours - 40
    regular_hours = 40
    overtime_wage = hourly_wage * 1.5
    weekly_wage = (regular_hours * hourly_wage) + (overtime_hours * overtime_wage)
else:
    weekly_wage = working_hours * hourly_wage

print(f"Your weekly wage is: {weekly_wage}€")