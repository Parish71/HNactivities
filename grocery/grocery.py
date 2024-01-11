def main():
    grocery_list = {}

    try:
        while True:
            item = input()
            item = item.lower()
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass

    print_grocery_list(grocery_list)


def print_grocery_list(grocery_list):
    sorted_items = sorted(grocery_list.items(), key=lambda x: x[0])

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()
