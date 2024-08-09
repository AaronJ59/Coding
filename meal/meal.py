def main():
    inputanswer = input("What time is it?")
    timeanswer = convert(inputanswer)
    if timeanswer >= 7 and timeanswer <= 8:
        print("breakfast time")
    if timeanswer >= 12 and timeanswer <= 13:
        print("lunch time")
    if timeanswer >= 18 and timeanswer <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    floatedminute = float(minutes) / 60
    return float(hours) + floatedminute


if __name__ == "__main__":
    main()