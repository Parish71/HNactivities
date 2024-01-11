import sys

def main():
    # Check the command line arguments
    check_command_arg()
    # Try to open the file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    # Handle the case where the specified file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Loop through the lines and check if starts with # or whitespace
    count = 0
    for line in lines:
        if check_line(line) == False:
            count += 1
    print(count)

def check_line(line):
    # Skip blank lines
    if line.isspace():
        return True
    # Check for inline comments and skip them
    if line.lstrip().startswith('#'):
        return True
    return False
    # Check for the start of a comment block
    #if line.lstrip().startswith("'''") or line.lstrip().startswith('"""'):
    #    return True
    # Check for the start or end of a docstring
    #if '"""' in line or "'''" in line:
    #    return True

    # Skip lines inside a comment block or docstring
    #if in_comment_block or in_docstring:
    #    continue


def check_command_arg():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        # Check if too few or too many arguments are provided
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
    # Check if the file has a .py extension
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    # Get the file path from the command-line argument
    file_path = sys.argv[1]


if __name__ == "__main__":
    main()
