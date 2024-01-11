# bank.py

def main():
    user_greeting = input("Greeting: ").strip().lower()
    result = value(user_greeting)
    print(f"${result}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and not greeting.startswith("hello"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
