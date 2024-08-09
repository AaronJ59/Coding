import re
import math


def main():
    number = input("Number: ")
    if check_number(number) == True:
        if algorithm_check(number) == True:
            print(card_brand(number))
        else:
            print("INVALID")
    else:
        print("INVALID")


def check_number(number):
    match = re.match(r"^(\d{13}|\d{15}|\d{16})$", number)

    if match:
        matches = re.match(r"^(4|34|37|51|52|53|54|55)", number)
        if matches:
            return True
    else:
        return False


def algorithm_check(n):
    number = int(n)

    denominator = 10
    num_list = []

    for _ in range(len(str(number))):
        digit = (number / denominator) % 10
        digit = math.trunc(digit)
        digit = digit * 2
        if digit > 9:
            digit_str = str(digit)
            first_digit = int(digit_str[0])
            second_digit = int(digit_str[1])
            num_list.append(first_digit)
            num_list.append(second_digit)
        else:
            num_list.append(digit)

        denominator = denominator * 100

    total_of_digits_multiplied = sum(num_list)
    num_list = []
    denominator = 1

    for _ in range(len(str(number))):
        digit = (number / denominator) % 10
        digit = math.trunc(digit)
        num_list.append(digit)
        denominator = denominator * 100

    total_of_digits = sum(num_list)

    total = (total_of_digits_multiplied + total_of_digits) % 10
    if total == 0:
        return True
    return False


def card_brand(n):
    n = str(n)
    match = re.match(r"^4", n)
    if match:
        return "VISA"
    match = re.match(r"^(34|37)", n)
    if match:
        return "AMEX"
    match = re.match(r"^(51|52|53|54|55)", n)
    if match:
        return "MASTERCARD"


main()
