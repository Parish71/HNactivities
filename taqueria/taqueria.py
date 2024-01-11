menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def calculate_total(order):
    return sum(menu[item] for item in order)

def main():
    order = []

    try:
        while True:
            item = input("Item: ").title()

            # Check if the entered item is on the menu
            if item in menu:
                order.append(item)
                total = calculate_total(order)
                print(f"Total: ${total:.2f}")
            else:
                print("")

    except EOFError:
        print("\n")  # Print a new line after catching EOFError

if __name__ == "__main__":
    main()
