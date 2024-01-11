def coke_machine():
    amount_due = 50
    total_inserted = 0

    while total_inserted < amount_due:
        print(f"Amount Due: {amount_due - total_inserted}")
        try:
            coin = int(input("Insert Coin: "))
            if coin in [25, 10, 5]:
                total_inserted += coin
            else:
                print("Invalid coin. Ignoring.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"Change Owed: {total_inserted - amount_due}")


if __name__ == "__main__":
    coke_machine()
