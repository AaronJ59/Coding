import random


def main():
    score = 0
    levelNumber = get_level()
    for i in range(10):
        x = generate_integer(levelNumber)
        y = generate_integer(levelNumber)
        print(str(x), "+", str(y), "= ", end="")
        answer = input()
        if not x + y == int(answer):
            for _ in range(2):
                print("EEE")
                print(str(x), "+", str(y), "= ", end="")
                answer = input()
                if x + y == int(answer):
                    score += 1
                    break
                elif _ == 1:
                    print(str(x), "+", str(y), "=", x + y)
                    break
        if x + y == int(answer):
            score += 1
    print("Score:", score)

def get_level():
    while True:
        try:
            levelNumber = int(input("Level: "))
            if levelNumber in [1, 2, 3]:
                return levelNumber
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)



if __name__ == "__main__":
    main()