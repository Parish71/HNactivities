#plates.py
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    for i in range(2, len(s)):
        if not s[i].isdigit():
            if s[i] == '0':
                return False
        else:
            break

    for i in range(2, len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    for char in s:
        if char in ['.', ' ', '?', '!']:
            return False

    return True

if __name__ == "__main__":
    main()
