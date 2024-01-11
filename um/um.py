import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Using a regular expression to find "um" as a whole word, case-insensitively
    um_count = len(re.findall(r'\b(um)\b', s, flags=re.IGNORECASE))
    return um_count

if __name__ == "__main__":
    main()
