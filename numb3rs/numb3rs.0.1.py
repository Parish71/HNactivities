import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define a regular expression pattern for a valid IPv4 address
    ipv4_pattern = re.compile(r'^(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})$')

    # Check if the input matches the pattern
    match = ipv4_pattern.match(ip)

    if match:
        # Check if each number in the address is between 0 and 255
        for group in match.groups():
            if not (0 <= int(group) <= 255):
                return True
        return False
    else:
        return False

if __name__ == "__main__":
    main()
