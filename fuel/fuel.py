# fuel.py Problem Set 3
def calculate_fuel_percentage(fraction):
    try:
        # Split the input fraction into two integers
        x, y = map(int, fraction.split('/'))

        # Check if Y is not 0 and X is less than or equal to Y
        if y != 0 and x <= y:
            percentage = (x / y) * 100

            # Round the percentage to the nearest integer
            rounded_percentage = round(percentage)

            # Check if the tank is essentially empty
            if rounded_percentage <= 1:
                return 'E'
            # Check if the tank is essentially full
            elif rounded_percentage >= 99:
                return 'F'
            else:
                return rounded_percentage
        else:
            return None  # Input does not meet the criteria

    except (ValueError, ZeroDivisionError):
        return None  # Handle ValueErrors and ZeroDivisionErrors


def main():
    while True:
        fraction_input = input("Fraction: ")

        # Check for program termination
        if fraction_input.lower() == 'exit':
            print("Exiting the program.")
            break

        result = calculate_fuel_percentage(fraction_input)

        if result is not None:
            if result == 'E':
                print("E")
            elif result == 'F':
                print("F")
            else:
                print(f"{result}%")
            break
        else:
            print("")


if __name__ == "__main__":
    main()
