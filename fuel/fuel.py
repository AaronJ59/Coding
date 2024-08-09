while True:
    try:
        frac = input("Fraction: ")
        num, den = frac.split("/")
        for char in num:
            if char in ["."]:
                print("Numerator is not an integer")
        for chara in den:
            if chara in ["."]:
                print("Numerator is not an integer")
        if int(num) > int(den) and not int(den) == 0:
            print("Numerator cannot be larger than denominator")
            continue
        percentage = int(num)/int(den)
        if percentage <= .01:
            print("E")
            break
        if percentage >= .99:
            print("F")
        else:
            newpercent = percentage * 100
            newpercent = str(round(newpercent))
            print(newpercent.replace(".0", "") + "%")


    except ValueError:
        print("That is not a fraction")
    except ZeroDivisionError:
        print("Denominator can not be zero")
    else:
        break
