import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = search_valid_format(s)

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = get_time_periods(match)

    start_hour, start_minute, end_hour, end_minute = convert_to_24_hour_format(start_hour, start_minute, start_period, end_hour, end_minute, end_period)

    validate_hours(start_hour, end_hour, start_minute, end_minute)

    return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"


def search_valid_format(s):
    # Define a pattern for both valid formats
    pattern = re.compile(r'^(\d{1,2})(?::(\d{1,2}))? (AM|PM) to (\d{1,2})(?::(\d{1,2}))? (AM|PM)$')
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid input format")

    return match


def get_time_periods(match):
    return match.groups()


def convert_to_24_hour_format(start_hour, start_minute, start_period, end_hour, end_minute, end_period):
    start_hour = int(start_hour)
    end_hour = int(end_hour)

    if start_period == 'PM' and start_hour != 12:
        start_hour += 12
    elif start_period == 'AM' and start_hour == 12:
        start_hour = 0

    if end_period == 'PM' and end_hour != 12:
        end_hour += 12
    elif end_period == 'AM' and end_hour == 12:
        end_hour = 0

    start_minute = int(start_minute) if start_minute is not None else 0
    end_minute = int(end_minute) if end_minute is not None else 0

    return start_hour, start_minute, end_hour, end_minute


def validate_hours(start_hour, end_hour, start_minute, end_minute):
    if not (0 <= start_hour <= 23) or not (0 <= end_hour <= 23) or not (0 <= start_minute <= 59) or not (0 <= end_minute <= 59):
        raise ValueError("Invalid hours")


if __name__ == "__main__":
    main()
