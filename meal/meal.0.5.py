def main():
    time_input = input("What time is it? ")

    if not (validate_time_format(time_input) or validate_12_hour_format(time_input)):
        print("Invalid time format. Please use HH:MM, HH:MM AM, or HH:MM PM.")
        return

    try:
        time_float = convert(time_input)
        determine_meal(time_float)
    except ValueError:
        print("Invalid time. Please enter a valid time in 24-hour or 12-hour format.")

def validate_time_format(time):
    # Check if the input is in the format HH:MM
    parts = time.split(":")
    return (
        len(time) == 5
        and time[2] == ":"
        and parts[0].isdigit() and len(parts[0]) <= 2
        and parts[1].isdigit() and len(parts[1]) == 2
    )

def validate_12_hour_format(time):
    # Check if the input is in the format HH:MM AM/PM
    return (
        len(time) == 8
        and time[2] == ":"
        and time[5] == " "
        and time[:2].isdigit() and len(time[:2]) <= 2
        and time[3:5].isdigit() and len(time[3:5]) == 2
        and (time[-4:] == "a.m." or time[-4:] == "p.m.")
    )

def convert(time):
    if validate_12_hour_format(time):
        hours, minutes, period = (
            time.split(":")[0].zfill(2),
            time.split(":")[1][:2],
            time.split(" ")[1],
        )
        if period == "p.m." and int(hours) != 12:
            hours = str(int(hours) + 12).zfill(2)
        elif period == "a.m." and int(hours) == 12:
            hours = "00"
        return float(hours) + float(minutes) / 60
    else:
        hours, minutes = map(int, time.split(":"))
        return hours + minutes / 60

def determine_meal(time_float):
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    if breakfast_start <= time_float <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= time_float <= lunch_end:
        print("lunch time")
    elif dinner_start <= time_float <= dinner_end:
        print("dinner time")

if __name__ == "__main__":
    main()
