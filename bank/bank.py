# bank.py

def main():

    user_greeting = input("Greeting: ").strip().lower()

    if user_greeting.startswith("hello"):
        print("$0")
    elif user_greeting.startswith("h") and not user_greeting.startswith("hello"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
