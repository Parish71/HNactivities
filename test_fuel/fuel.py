# fuel.py

def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y != 0 and x <= y:
            percentage = (x / y) * 100
            return round(percentage)
        else:
            return 0  # Return a default value for invalid input

    except (ValueError, ZeroDivisionError):
        return 0  # Return a default value for invalid input

def gauge(percentage):
            # Check if the tank is essentially empty
        if percentage <= 1:
            return 'E'
        # Check if the tank is essentially full
        elif percentage >= 99:
            return 'F'
        else:
            return f'{percentage}%'

def main():
    while True:
        fraction_input = input("Fraction: ")

        # Check for program termination
        if fraction_input.lower() == 'exit':
            print("Exiting the program.")
            break

        percentage = convert(fraction_input)
        result = gauge(percentage)

        if result is not None:
            print(result)
            break


if __name__ == "__main__":
    main()
