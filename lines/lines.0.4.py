import sys

def read_lines_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Error: File does not exist")
        sys.exit(1)

def is_comment_block(line):
    return line.lstrip().startswith("'''") or line.lstrip().startswith('"""')

def is_multiline_docstring(line, in_multiline_docstring):
    return '"""' in line or "'''" in line or in_multiline_docstring

def is_inline_comment(line):
    return '#' in line

def is_blank_line(line):
    return line.strip() == ''

def count_lines_of_code(lines):
    count = 0
    in_comment_block = False
    in_multiline_docstring = False

    for line in lines:
        if is_comment_block(line):
            in_comment_block = not in_comment_block

        in_multiline_docstring = is_multiline_docstring(line, in_multiline_docstring)

        if in_comment_block or in_multiline_docstring:
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

