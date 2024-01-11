def main():
    user_input = input("Input: ")
    output_text = shorten(user_input)
    print("Output:", output_text)

def shorten(word):
    vowels = "AEIOUaeiou"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()
