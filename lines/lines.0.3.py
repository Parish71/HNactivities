import sys

def count_lines(file_path):
    """
    Count the number of lines of code in a Python file, excluding comments and blank lines.

    Args:
    - file_path (str): The path to the Python file.

    Returns:
    - int: The number of lines of code.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        count = 0
        in_comment_block = False

        for line in lines:
            # Check for the start of a comment block
            if line.lstrip().startswith("'''") or line.lstrip().startswith('"""'):
                in_comment_block = not in_comment_block

            # Skip lines inside a comment block
            if in_comment_block:
                continue

            # Check for inline comments and skip them
            if '#' in line:
                line = line.split('#')[0]

            # Skip blank lines
            if line.strip() == '':
                continue

            count += 1

        return count

    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("Too many command-line arguments")
        sys.exit()

    # Get the file path from the command-line argument
    file_path = sys.argv[1]

    # Check if the file has a .py extension
    if not file_path.endswith(".py"):
        print("Not a Python file")
        sys.exit()

    # Count lines and print the result
    lines_count = count_lines(file_path)
    print(lines_count)
