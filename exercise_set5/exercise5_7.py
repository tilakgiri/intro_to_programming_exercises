# using the list items given in moodle
products = ["PHILIPS_Boiler_HD4646_2020_09_21_C_1",
            "KENWOOD_KitchenMachine_KVL8300S_2015_09_22_C_3",
            "BOSCH_Blender_MMB65G5M_2016_05_07_C_3",
            "WHIRLPOOL_Microwave_MCP345WH_2019_01_15_C_1",
            "ROSENLEW_Freezer_RPP2330_2017_01_29_C_2",
            "ELECTROLUX_Fridge_ERF4114AOW_2017_11_07_C_2"]
categories = ["Other", "Small electronics", "Appliances", "Blenders"]

# for loop that goes through every element in list
for product in products:
    product = product.split("_")

    # storing the split data into respective variables as asked in exercise
    brand = product[0]
    product_name = product[1]
    model = product[2]
    year = product[3]
    month = product[4]
    day = product[5]

    # since the category name depends on the number from list element
    # i used if-else condition to check and give their respective names
    category_number = product[7]
    if category_number == "1":
        description = categories[1]
    elif category_number == "2":
        description = categories[2]
    elif category_number == "3":
        description = categories[3]
    else:
        description = categories[0]

    # printing every line as required from the program
    print(f"Brand: {brand}")
    print(f"Name and model: {product_name} ({model})")
    print(f"Category: {description}")
    print(f"Addition date: {day}.{month}.{year}\n")


# no AI has been used to write this program :)