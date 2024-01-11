from validator_collection import validators, errors

def validate_email():
    try:
        email_address = validators.email(input("What's your email address? "))
        print("Valid")
    except errors.EmptyValueError:
        print("Invalid")
    except errors.InvalidEmailError:
        print("Invalid")

if __name__ == "__main__":
    validate_email()
