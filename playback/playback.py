# Define a fuction called "main" to encapsulate the main logic of the program.
def main():
    # Prompt the user to input a phrase and store it in a variable "user_input".
    user_input = input()

    # Replace all occurrences of spaces in the user input with "..."
    modified_phrase = user_input.replace(" ", "...")

    # Display the modified phrase to the user.
    print(modified_phrase)

# Check if the current script is being ruin as the main program.
if __name__ == "__main__":

    main()
