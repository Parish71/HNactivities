import sys
import csv
from tabulate import tabulate

def load_csv(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            # Assuming the CSV file has a header row
            reader = csv.DictReader(csvfile)
            # Extract headers
            headers = reader.fieldnames
            # Convert list of dictionaries to list of lists
            data = [list(row.values()) for row in reader]
        return headers, data
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    if len(sys.argv) != 2:
        # Check if too few or too many arguments are provided
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)

    # Extract the file path from command-line arguments
    csv_file_path = sys.argv[1]

    # Check if the file name ends with '.csv'
    if not csv_file_path.lower().endswith('.csv'):
        sys.exit("Not a CSV file")

    # Load data from the CSV file along with headers
    headers, table_data = load_csv(csv_file_path)

    # Print the table using tabulate in grid format with headers
    formatted_table = tabulate(table_data, headers=headers, tablefmt="grid")
    print(formatted_table)

if __name__ == "__main__":
    main()
