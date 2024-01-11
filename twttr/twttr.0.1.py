def remove_vowels(text):
    vowels = "AEIOUaeiou"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

def main():
    user_input = input("Input: ")
    output_text = remove_vowels(user_input)
    print("Output:", output_text)

if __name__ == "__main__":
    main()
