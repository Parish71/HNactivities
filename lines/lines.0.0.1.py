import sys

def read_lines_from_file(file_path):
    """
    Read lines from the specified file.

    Args:
    - file_path (str): The path to the file.

    Returns:
    - list: A list containing lines from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Error: File does not exist")
        sys.exit(1)

def is_comment_block(line):
    """
    Check if the line starts a comment block.

    Args:
    - line (str): The line to check.

    Returns:
    - bool: True if the line starts a comment block, False otherwise.
    """
    return line.lstrip().startswith("'''") or line.lstrip().startswith('"""')

def is_docstring(line):
    """
    Check if the line is part of a docstring.

    Args:
    - line (str): The line to check.

    Returns:
    - bool: True if the line is part of a docstring, False otherwise.
    """
    return '"""' in line or "'''" in line

def is_inline_comment(line):
    """
    Check if the line contains an inline comment.

    Args:
    - line (str): The line to check.

    Returns:
    - bool: True if the line contains an inline comment, False otherwise.
    """
    return '#' in line

def is_blank_line(line):
    """
    Check if the line is blank.

    Args:
    - line (str): The line to check.

    Returns:
    - bool: True if the line is blank, False otherwise.
    """
    return line.strip() == ''

def count_lines_of_code(lines):
    """
    Count the number of lines of code, excluding comments and blank lines.

    Args:
    - lines (list): List of lines to process.

    Returns:
    - int: The number of lines of code.
    """
    count = 0
    in_comment_block = False
    in_docstring = False

    for line in lines:
        if is_comment_block(line):
            in_comment_block = not in_comment_block

        if is_docstring(line):
            in_docstring = not in_docstring

        if in_comment_block or in_docstring:
            continue

        if is_inline_comment(line):
            line = line.split('#')[0]

        if is_blank_line(line):
            continue

        count += 1

    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Incorrect number of command-line arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith(".py"):
        print("Error: Not a Python file (file must have a .py extension)")
        sys.exit(1)

    lines = read_lines_from_file(file_path)
    lines_count = count_lines_of_code(lines)
    print(lines_count)
