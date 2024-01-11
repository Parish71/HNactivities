import re

def convert_to_iso(date_str):
    # Define a list of months
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Attempt to match the input against the three possible formats
    match_date_format1 = re.match(r'(\d{1,2})/(\d{1,2})/(\d{4})', date_str)
    match_date_format2 = re.match(r'(\d{1,2}) (\w+) (\d{4})', date_str)
    match_date_format3 = re.match(r'(\w+) (\d{1,2}), (\d{4})', date_str)

    if match_date_format1:
        month, day, year = map(int, match_date_format1.groups())
    elif match_date_format2:
        day, month_str, year = match_date_format2.groups()
        month = months.index(month_str) + 1
    elif match_date_format3:
        month_str, day, year = match_date_format3.groups()
        month = months.index(month_str) + 1
        day = int(day)
    else:
        return None  # Invalid date format

    # Validate the month and day
    if month < 1 or month > 12 or day < 1 or day > 31:
        return None  # Invalid date

    # Format the date in ISO 8601 (YYYY-MM-DD)
    return f"{year:04}-{month:02d}-{day:02d}"

def main():
    while True:
        user_input = input("Date: ")
        iso_date = convert_to_iso(user_input)

        if iso_date:
            print(iso_date)
            break
        else:
            print("")

if __name__ == "__main__":
    main()
