import re
import emoji

def custom_emoji_replace(match):
    alias = match.group(1)
    emoji_char = emoji.emojize(f":{alias}:", variant="emoji_type")
    return emoji_char if emoji_char else match.group(0)

def emojize_text(input_text):
    # Adicione a substituição para transformar _ em ""
    input_text = re.sub(r':([a-zA-Z0-9]+)_([a-zA-Z0-9]+):', r':\1\2:', input_text)

    custom_emoji_pattern = re.compile(r':([a-zA-Z0-9_]+):')
    return custom_emoji_pattern.sub(custom_emoji_replace, input_text)

def main():
    user_input = input("Input: ")
    emojized_text = emojize_text(user_input)
    print(emojized_text)

if __name__ == "__main__":
    main()
