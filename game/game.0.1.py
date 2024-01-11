import random

def main():
    while True:
        try:
            level = int(input("Enter a positive integer for the level: "))
            if level > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid number.")

    # Randomly generate a number between 1 and level
    secret_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess < 1:
                print("Please enter a positive integer.")
                continue

            if guess < secret_number:
                print("Too small!")
            elif guess > secret_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
