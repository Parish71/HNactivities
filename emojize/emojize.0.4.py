import re
import emoji

def custom_emoji_replace(match):
    alias = match.group(1)
    emoji_char = emoji.emojize(f":{alias}:", use_aliases=True)
    return emoji_char if emoji_char else match.group(0)

def emojize_text(input_text):
    custom_emoji_pattern = re.compile(r':([a-zA-Z0-9_]+):')
    return emoji.emojize(input_text, variant="emoji_type")

def main():
    user_input = input("Input: ")
    emojized_text = emojize_text(user_input)
    print(emojized_text)

if __name__ == "__main__":
    main()
