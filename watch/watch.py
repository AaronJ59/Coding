import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if "<iframe" in s:
        matches = re.search(r"(https?)://(www.)?youtube\.com/embed/xvFZjo5PgG0", s)
        if matches:
            return("https://youtu.be/xvFZjo5PgG0")
    else:
        return None



...


if __name__ == "__main__":
    main()