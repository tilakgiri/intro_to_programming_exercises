text = input("Give some text:\n")

reverse_text = text[::-1]
print(reverse_text)

if text == "":
    print("Your text is empty.\n")
elif text == reverse_text:
    print("Palindrome: YES\n")
else:
    print("Palindrome: NO\n")