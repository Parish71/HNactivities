import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
            else:
                print("")
        except ValueError:
            print("")

    # Randomly generate a number between 1 and level
    # If level is 1, the number will always be 1
    secret_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                print("")
                continue

            if guess < secret_number:
                print("Too small!")
            elif guess > secret_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("")

if __name__ == "__main__":
    main()
