points = input("Exam points:\n")
points = int(points)

if 0 <= points <= 50:
    print("Grade: 0\n")
elif 51 <= points <= 60:
    print("Grade: 1\n")
elif 61 <= points <= 70:
    print("Grade: 2\n")
elif 71 <= points <= 80:
    print("Grade: 3\n")
elif 81 <= points <= 90:
    print("Grade: 4\n")
elif 91 <= points <= 100:
    print("Grade: 5\n")
else:
    print("Invalid points value.\n")