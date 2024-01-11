import sys
import csv

def load_csv(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            # Assuming the CSV file has a header row
            reader = csv.DictReader(csvfile)
            # Extract headers
            headers = reader.fieldnames
            # Extract data
            data = [row for row in reader]

        return headers, data
    except FileNotFoundError:
        sys.exit(f"Could not read {file_path}")

def convert_and_write_csv(input_file, output_file):
    headers, table_data = load_csv(input_file)

    # Create a new CSV file with columns first, last, and house
    output_headers = ['first', 'last', 'house']

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=output_headers)

        # Write the header to the output CSV
        writer.writeheader()

        # Convert and write each row to the output CSV
        for entry in table_data:
            # Assuming 'name' is the column in your CSV
            full_name = entry.get('name', '')

            # Split the full name into first name and last name
            parts = full_name.split(', ')
            last_name = parts[0]
            first_name = parts[1] if len(parts) > 1 else ''

            # Write the converted data to the output CSV
            writer.writerow({'first': first_name, 'last': last_name, 'house': entry.get('house', '')})

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) !=3:
        #Check if to few args are provided
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
            sys.exit(1)
        if len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)

    # Extract the file paths from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file name ends with '.csv'
    if not input_file.lower().endswith('.csv'):
        sys.exit("Input file is not a csv file")

    # Call the function to convert and write the CSV
    convert_and_write_csv(input_file, output_file)
    print(f"Conversion complete. Output written to {output_file}")

if __name__ == "__main__":
    main()
