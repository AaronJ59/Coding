from datetime import date, datetime
import inflect
import re
import sys

class WrongFormatError(Exception):
    pass

class Time:
    def __init__(self, dob):
        matches = re.search(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", dob)
        if matches:
            self.year = int(matches.group(1))
            self.month = int(matches.group(2))
            self.day = int(matches.group(3))
        else:
            sys.exit("Format is wrong")



    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if year > datetime.now().year:
            sys.exit("Year is too ahead")
        else:
            self._year = year


    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if month > 12 or month < 1:
            sys.exit("Month number does not make sense")
        else:
            self._month = month

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        try:
            date(self.year, self.month, day)
        except ValueError:
            sys.exit("The day number is not correct")
        self._day = day




def main():
    time_instance = input("Date of Birth: ")
    time_obj = Time(time_instance)
    days_extracted = minutes_to_days(time_obj)
    spelled_out = days_to_min_in_words(days_extracted)
    print(spelled_out)


def minutes_to_days(s):
    dateofbirth = datetime(s._year, s._month, s._day, 0, 0, 0)
    datenow = date.today()
    year_now = datenow.year
    month_now = datenow.month
    day_now =  datenow.day
    datenow = datetime(year_now, month_now, day_now, 0, 0, 0)
    days_since_dob = datenow - dateofbirth
    days = str(days_since_dob).replace(" days, 0:00:00", "")
    return days



def days_to_min_in_words(s):
    minutes = int(s) * 1440
    p = inflect.engine()
    minutes_in_words = p.number_to_words(minutes, andword="")
    return f"{minutes_in_words.capitalize()} minutes"


...


if __name__ == "__main__":
    main()