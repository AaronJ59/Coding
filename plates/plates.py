def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")




def is_valid(vanity):
    if len(vanity) < 2:
        return False
    firsttwoletters = vanity[0:2]
    if not firsttwoletters.isalpha():
        return False
    if len(vanity) < 2 or len(vanity) > 6:
        return False
    restof = vanity[2:]

    numberspotted = False
    digitcount = 0

    for char in restof:
        if char.isdigit():
            numberspotted = True
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                digitcount = digitcount + 1
            if char == "0" and digitcount == 0:
                return False
        elif char.isalpha():
            if numberspotted:
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    main()







