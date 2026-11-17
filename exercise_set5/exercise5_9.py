# imaginary person's names
names = ["Isha",    "Bijay",    "Bibek",    "Bimal",
         "Hari",    "Niraj",    "Badal",    "Muttaswami Venugopal Iyar",
         "Venugopal Iyer",    "Iyer"]
vowels = "aeiou"

# vowels = ["a", "e", "i", "o", "u"]
names = [name.lower() for name in names]
filtered_names = [name for name in names if "s" not in name]
filtered_names = [name for name in filtered_names if "e" not in name]
filtered_names = [name for name in filtered_names if len(name) < 8]

# filtered_names = [sum(map(filtered_names.count, vowels)) <= 2]

# for name in filtered_names:
#     count = sum(map(name.count, vowels)) <= 2
#     filtered_names =

print(filtered_names)