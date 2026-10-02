import math

# known mathematical equations available.
cherry_pair = 2 + 2 * 2 + 2 - 2 - 2
cherry = cherry_pair / 2
apple = ((math.sqrt(3 + 10 - 4)/3) + ((math.pow(5 , 3)-5)/20) + 3)

# apple - orange = 9
# orange = apple - 9 (this is the basic mathematical equation we can make)
orange = apple - 9
two_oranges = orange * 2

# cherry_pair - three_banana = 10
# three_banana = cherry_pair - 10
three_banana = cherry_pair - 10

# now we need value of one banana
# to figure our final caluclation.
one_banana = three_banana / 3
two_bananas = one_banana * 2

# three_banana + pear = 8
# pear = 8 - three_banana
pear = 8 - three_banana

# we also need a pear + a cherry 
pear_cherry = pear + cherry

# final calculation
final_calculation = apple + two_bananas + two_oranges + pear_cherry

print(f"Result: {final_calculation}")