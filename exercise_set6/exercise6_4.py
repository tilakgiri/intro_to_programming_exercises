# product identifiers list copied from moodle
products = ["K1565_2017_ST7745", "T2432_2019_FE84",
            "T8551_2018_XA413", "T3345_2019_JK142",
            "Y51372_2019_HJ2", "Y76715_2017_AB3",
            "E98144_2018_21T", "T7733_2020_CE55",
            "E7614_2021_XZA784", "E9722_2017_MHE67",
            "Y82018_2020_FI95", "T61287_2021_IA293",
            "E9152_2019_TY5", "T774_2021_OB672"]


# year demanded by the user to be searched
demand_year = input("Search code for which year?:\n")
demand_year = int(demand_year)

# loops through every product identifier
for product in products:
    # splitting identifier by "_" for ease
    product = product.split("_")
    # data year is the year separated from product identifier
    data_year = int(product[1])
    # if the match is found we print the order code in index 0
    if data_year == demand_year:
        print(product[0])


# no AI is used to write this code