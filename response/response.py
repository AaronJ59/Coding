import validators


def main():
    validorinvalid = check_email(input("What's your email? "))
    if validorinvalid == None:
        print("Invalid")
    if validorinvalid == "Valid":
        print("Valid")


def check_email(email):
    return_value = validators.email(email)
    if return_value == True:
        return "Valid"
    """
    When the "if return_value == True" condition doesn't run, check_email() will return None.
    """


if __name__ == "__main__":
    main()
