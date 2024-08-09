text = input("Text: ")


word_count = 1
letter_count = 0
sentence_count = 0


for char in text:
    if char.isalpha():
        letter_count = letter_count + 1
    if char.isspace():
        word_count = word_count + 1
    if char in [".", "?", "!"]:
        sentence_count = sentence_count + 1


L = (letter_count / word_count) * 100
S = (sentence_count / word_count) * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
