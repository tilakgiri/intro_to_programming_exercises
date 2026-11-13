# boolean for running the program repeatedly
run = True

# this code block works until user gives 0
while run:
    table_for = input("Which multiplication table would you like to see? (1-10). 0 stops program\n")
    table_for = int(table_for)

    # this breaks the loop if input is 0
    if table_for == 0:
        break

    # this is the main part which creates the table if everything is right
    elif 1 <= table_for <= 10:
        for table in range(10):
            table += 1
            result = table_for * table

            print(f"{table_for} * {table} = {result}")
    # condition for when the input is undesirable.
    else:
        print("Wrong number format.\n")

# no AI has been used to write this code :)