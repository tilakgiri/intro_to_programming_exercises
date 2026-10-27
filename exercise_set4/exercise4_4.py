try:
    first_number = input("First number:\n")
    first_number = int(first_number)
    second_number = input("Second number:\n")
    second_number = int(second_number)
    
    result = first_number / second_number
    print(f"{result}")
except ValueError:
    print("Incorrect format.")
except ZeroDivisionError:
    print("You can't divide by zero.")