from cs50 import get_int

while True:
    height = get_int("Height: ")

    if height >= 1 and height <= 8:
        break

num_of_space = height - 1
hashtag_count = 1
for i in range(height):
    print(" " * num_of_space, end="")
    print("#" * hashtag_count, end="")
    print("  ", end="")
    print("#" * hashtag_count)
    num_of_space = num_of_space - 1
    hashtag_count = hashtag_count + 1
