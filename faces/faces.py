
conversion_dict = {
    ":)": "🙂",
    ":(": "🙁",
}




# Function to convert ":)" to a smile face emoji
def convert(input_str):
    for emoticon, emoji in conversion_dict.items():
        input_str = input_str.replace(emoticon, emoji)
    return input_str



# Define a fuction called "main" to encapsulate the main logic of the program.
def main():
    # Prompt the user to input a phrase and store it in a variable "user_input".
    user_input = input()
    # Call the "convert" function to process the user input and store the result in "converted_input".
    modified_phrase = convert(user_input)
    # Display the converted input.
    print(modified_phrase)

# Check if the current script is being ruin as the main program.
if __name__ == "__main__":

    main()
