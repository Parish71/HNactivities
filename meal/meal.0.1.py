def main():
    time_input = input("Enter the time in 24-hour format (HH:MM): ")

    # Check if the input is in the correct format
    if len(time_input) != 5 or time_input[2] != ":":
        print("Invalid time format. Please use HH:MM.")
        return

    try:
        time_float = convert(time_input)
        determine_meal(time_float)
    except ValueError:
        print("Invalid time. Please enter a valid time in 24-hour format.")

def convert(time):
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
        print("It's breakfast time!")
    elif lunch_start <= time_float <= lunch_end:
        print("It's lunch time!")
    elif dinner_start <= time_float <= dinner_end:
        print("It's dinner time!")

if __name__ == "__main__":
    main()
