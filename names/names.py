
"""
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""
# The code above allowed me to write the names on the names.txt file.
"""
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
"""
#The code above allowed me to print the names that are on the file "names.txt" as it is shown and not in alphabetical order

"""
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
"""
# The code above allows me to append the names in the names.txt file into the names list. Then, I can sort the names in order and then print them out
# I also don't need to to write "r", If it is removed, the function will work the same. By default, open() has "r"

