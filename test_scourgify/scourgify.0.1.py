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
            # Extract the file path from command-line arguments
            file_path = sys.argv[1]

        return headers, data
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def main():
    if len(sys.argv) !=3:
        #Check if to few args are provided
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
            sys.exit(1)
        if len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)


    # Check if the file name ends with '.csv'
    if not file_path.lower().endswith('.csv'):
        sys.exit("Not a csv file")

    headers, table_data = load_csv(csv_file_path)



if __name__ == "__main__":
    main()
