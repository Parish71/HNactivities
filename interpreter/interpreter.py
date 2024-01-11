# interpreter.py

def main():
    # Prompt the user for an arithmetic expression
    expression = input("Please enter an arithmetic expression (x y z): ")

    # Split the expression into x, y, and z
    x, y, z = expression.split(" ")

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Perform the arithmetic operation based on y
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z
    else:
        print("Invalid operator.")
        return

    # Output the result formatted to one decimal place
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
