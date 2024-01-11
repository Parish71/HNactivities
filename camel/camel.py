def camel_to_snake(variable_name):
    snake_case_name = ""

    for char in variable_name:

        if char.isupper():

            snake_case_name += "_" + char.lower()
        else:
            snake_case_name += char

    # If the name starts with an uppercase letter, remove the leading underscore
    if snake_case_name.startswith("_"):
        snake_case_name = snake_case_name[1:]

    return snake_case_name

def main():
    camel_case_input = input("camelCase: ")
    snake_case_output = camel_to_snake(camel_case_input)
    print(f"snake_case: {snake_case_output}")

if __name__ == "__main__":
    main()
