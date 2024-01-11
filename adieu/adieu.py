import inflect

def main():
    names = []
    p = inflect.engine()

    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        adieu(names, p)

def adieu(names, p):
    if len(names) > 1:
        formatted_names = p.join(names)
    else:
        formatted_names = names[0]

    print(f"Adieu, adieu, to {formatted_names}")

if __name__ == "__main__":
    main()
