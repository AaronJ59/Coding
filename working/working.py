import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"([0-9]{1,2}):?([0-9]{2})? (AM|PM) to ([0-9]{1,2}):?([0-9]{2})? (AM|PM)", s)
    if matches:
        firsthour = matches.group(1)
        firstminute = matches.group(2)
        sechour = matches.group(4)
        secminute = matches.group(5)

        if int(firsthour) <= 0 or int(firsthour) > 12 or int(sechour) <= 0 or int(sechour) > 12:
                raise ValueError("Hour is wrong format")

        if sechour == "12" and matches.group(6) == "AM":
            sechour = "00"
        elif sechour == "12" and matches.group(6) == "PM":
            sec_hour_military_pm = "12"
        else:
            sec_hour_military_pm = int(sechour) + 12

        if firsthour == "12" and matches.group(3) == "PM":
            first_hour_military_pm = "12"
        elif firsthour == "12" and matches.group(3) == "AM":
            firsthour = "0"
        else:
            first_hour_military_pm = int(firsthour) + 12





        if matches.group(2) is None and matches.group(5) is None: # This line and the code below will execute if the minutes were not written down. Ex: 9 AM to 10 PM
            if matches.group(3) == "AM" and matches.group(6) == "PM":
                if len(firsthour) == 1 and len(sechour) == 1:
                    return f"0{firsthour}:00 to {sec_hour_military_pm}:00"
                if len(firsthour) == 2 and len(sechour) == 1:
                    return f"{firsthour}:00 to {sec_hour_military_pm}:00"
                if len(firsthour) == 1 and len(sechour) == 2:
                    return f"0{firsthour}:00 to {sec_hour_military_pm}:00"
                if len(firsthour) == 2 and len(sechour) == 2:
                    return f"{firsthour}:00 to {sec_hour_military_pm}:00"
            if matches.group(3) == "AM" and matches.group(6) == "AM":
                if len(firsthour) == 1 and len(sechour) == 1:
                    return f"0{firsthour}:00 to 0{sechour}:00"
                if len(firsthour) == 2 and len(sechour) == 1:
                    return f"{firsthour}:00 to 0{sechour}:00"
                if len(firsthour) == 1 and len(sechour) == 2:
                    return f"0{firsthour}:00 to {sechour}:00"
                if len(firsthour) == 2 and len(sechour) == 2:
                    return f"{firsthour}:00 to {sechour}:00"
            if matches.group(3) == "PM" and matches.group(6) == "AM":
                if len(firsthour) == 1 and len(sechour) == 1:
                    return f"{first_hour_military_pm}:00 to 0{sechour}:00"
                if len(firsthour) == 2 and len(sechour) == 1:
                    return f"{first_hour_military_pm}:00 to 0{sechour}:00"
                if len(firsthour) == 1 and len(sechour) == 2:
                    return f"{first_hour_military_pm}:00 to {sechour}:00"
                if len(firsthour) == 2 and len(sechour) == 2:
                    return f"{first_hour_military_pm}:00 to {sechour}:00"
            if matches.group(3) == "PM" and matches.group(6) == "PM":
                if len(firsthour) == 1 and len(sechour) == 1:
                    return f"{first_hour_military_pm}:00 to {sec_hour_military_pm}:00"
                if len(firsthour) == 2 and len(sechour) == 1:
                    return f"{first_hour_military_pm}:00 to {sec_hour_military_pm}:00"
                if len(firsthour) == 1 and len(sechour) == 2:
                    return f"{first_hour_military_pm}:00 to {sec_hour_military_pm}:00"
                if len(firsthour) == 2 and len(sechour) == 2:
                    return f"{first_hour_military_pm}:00 to {sec_hour_military_pm}:00"



        if int(matches.group(2)) >= 0 and int(matches.group(5)) >= 0: # This line checks if the minutes were also inputted. Ex: 9:50 AM to 10:37 PM
            if int(firstminute) < 0 or int(firstminute) > 59 or int(secminute) < 0 or int(secminute) > 59:
                raise ValueError("Minutes are wrong format")
            if matches.group(3) == "AM" and matches.group(6) == "PM":
                if len(firsthour) == 1 and len(sechour) == 1:
                    return f"0{firsthour}:{firstminute} to {sec_hour_military_pm}:{secminute}"
                if len(firsthour) == 2 and len(sechour) == 1:
                    return f"{firsthour}:{firstminute} to {sec_hour_military_pm}:{secminute}"
                if len(firsthour) == 1 and len(sechour) == 2:
                    return f"0{firsthour}:{firstminute} to {sec_hour_military_pm}:{secminute}"
                if len(firsthour) == 2 and len(sechour) == 2:
                    return f"{firsthour}:{firstminute} to {sec_hour_military_pm}:{secminute}"
            if matches.group(3) == "AM" and matches.group(6) == "AM":
                if len(firsthour) == 1 and len(sechour) == 1:
                    return f"0{firsthour}:{firstminute} to 0{sechour}:{secminute}"
                if len(firsthour) == 2 and len(sechour) == 1:
                    return f"{firsthour}:{firstminute} to 0{sechour}:{secminute}"
                if len(firsthour) == 1 and len(sechour) == 2:
                    return f"0{firsthour}:{firstminute} to {sechour}:{secminute}"
                if len(firsthour) == 2 and len(sechour) == 2:
                    return f"{firsthour}:{firstminute} to {sechour}:{secminute}"
            if matches.group(3) == "PM" and matches.group(6) == "AM":
                if len(firsthour) == 1 and len(sechour) == 1:
                    return f"{first_hour_military_pm}:{firstminute} to 0{sechour}:{secminute}"
                if len(firsthour) == 2 and len(sechour) == 1:
                    return f"{first_hour_military_pm}:{firstminute} to 0{sechour}:{secminute}"
                if len(firsthour) == 1 and len(sechour) == 2:
                    return f"{first_hour_military_pm}:{firstminute} to {sechour}:{secminute}"
                if len(firsthour) == 2 and len(sechour) == 2:
                    return f"{first_hour_military_pm}:{firstminute} to {sechour}:{secminute}"
            if matches.group(3) == "PM" and matches.group(6) == "PM":
                if len(firsthour) == 1 and len(sechour) == 1:
                    return f"{first_hour_military_pm}:{firstminute} to {sec_hour_military_pm}:{secminute}"
                if len(firsthour) == 2 and len(sechour) == 1:
                    return f"{first_hour_military_pm}:{firstminute} to {sec_hour_military_pm}:{secminute}"
                if len(firsthour) == 1 and len(sechour) == 2:
                    return f"{first_hour_military_pm}:{firstminute} to {sec_hour_military_pm}:{secminute}"
                if len(firsthour) == 2 and len(sechour) == 2:
                    return f"{first_hour_military_pm}:{firstminute} to {sec_hour_military_pm}:{secminute}"
    else:
        raise ValueError("Wrong format")






...


if __name__ == "__main__":
    main()