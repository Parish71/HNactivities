import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Use re.search directly to check if the input matches the pattern
    if re.search(r'^(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})$', ip):
        list_of_groups = ip.split(".")
        for group in list_of_groups:
            if 0 > int(group) or int(group) > 255:
                return False
        # If all groups pass the check, return True
        return True

    # If no match is found, return False
    return False

if __name__ == "__main__":
    main()
