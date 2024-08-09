import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if matches:
        for str_number in matches.groups():
            if int(str_number) < 0 or int(str_number) > 255:
                return False
        return True
    else:
        return False




...


if __name__ == "__main__":
    main()