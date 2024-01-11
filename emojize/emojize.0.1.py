import emoji

def emojize_text(input_text):

    alias_mapping = {
        ':smile_cat:': ':😸:'
    }

    for alias, shortcode in alias_mapping.items():
        input_text = input_text.replace(alias, shortcode)

    return emoji.emojize(input_text, variant="emoji_type")

def main():
    while True:
        user_input = input("Input: ")
        if user_input.lower() in ['exit', 'quit', 'q']:
            break
        emojized_text = emojize_text(user_input)
        print("Output:", emojized_text)

if __name__ == "__main__":
    main()
