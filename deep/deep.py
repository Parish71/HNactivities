def main():
    # Prompt the user for the answer to the Great Question of Life, the Universe, and Everything
    user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # Normalize the imput to make the comparison case-insesitive
    normalized_input  = user_input.lower().replace("-"," ").strip()

    # Check if the user's input is either "42", "forty-two", or "forty two"
    if normalized_input == "42" or normalized_input == "forty two":
        print("Yes")
    else:
        print("No")

# Call the main fuction to execute the program
if __name__ == "__main__":
    main()