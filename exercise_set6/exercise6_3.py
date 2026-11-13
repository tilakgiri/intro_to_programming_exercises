students = input("How many students?\n")
students = int(students)

total = 0

for student in range(students):
    grade = input("Student grade:\n")
    grade = int(grade)
    total += grade

average = total / students
print(f"Average grade: {average}")


if 0<= average < 1:
    print("Bad result")
elif 1<= average < 2:
    print("Weak result")
elif 2<= average < 3:
    print("Average result")
elif 3<= average < 4:
    print("Good result")
elif 4<= average < 5:
    print("Excellent result")
else:
    print("Invalid result")