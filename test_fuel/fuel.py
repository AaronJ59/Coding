
def main():
    frac = input("Fraction: ")
    roundednumber = convert(frac)
    if roundednumber is None:
        return
    result = gauge(roundednumber)
    print(result)


def convert(fraction):
    while True:
        try:
            num, den = fraction.split("/")
            if "." in num:
                raise ValueError
            if "." in den:
                raise ValueError
            if int(num) > int(den) and not int(den) == 0:
                raise ValueError
            if int(den) == 0:
                raise ZeroDivisionError
            percentage = int(num)/int(den)
            percentage = percentage * 100
            percentagerounded = round(percentage)
            return percentagerounded

        except(ValueError,ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()