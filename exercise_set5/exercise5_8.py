# taking input for text and shift number
user_txt = input("Enter the text to perform Caesar's Cipher:\n")
shift_num = input("Enter the shift number for Ceaser Cipher:\n")
shift_num = int(shift_num)
converted_txt = ""

# for loop that goes through every character in user_txt
for char in user_txt:
    # new shifted character is old character order + shift number
    # which can be done in this way
    shifted_char = ord(char) + shift_num
    # now adding the shifted character into converted_txt variable
    # which at the end gives us the final converted txt
    converted_txt += chr(shifted_char)
# printing outside the loop for the obvious reasons
print(converted_txt)


# no AI had been used to write this code
# the tips in exercises were taken into consideration



