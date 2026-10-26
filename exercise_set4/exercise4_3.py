text = "The quick brown fox jumps over the lazy dog. That sentence contains every letter in the English alphabet. Neat!"
print(f"{text}\n")

text = text.replace("fox", "duck")
print(f"{text}\n")

remove = input("Which word should be removed?:\n")
if remove in text:
    text = text.replace(remove, "")
    print(f"{text}\n")
else:
    print("Word not found.\n")

length = len(text)
print(f"{length} characters.\n")

word_count = len(text.split())
print(f"{word_count} words.\n")

text = text.replace(".", "\n")
print(f"{text}\n")

user_text = input("Write a new sentence:\n")
user_text_length = len(user_text)

print(f"{user_text_length}\n")

if user_text_length < 20:
    print(f"{user_text}\n")
else:
    user_text = user_text[0:20]
    print(f"{user_text}...\n")

