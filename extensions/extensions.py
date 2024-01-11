# extensions.py

def main():
    # Prompt the user for the name of a file
    file_name = input("File name: ").strip().lower()

    # Dictionary to map file extensions to media types
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Extract the file extension from the file name
    file_extension = ''
    if '.' in file_name:
        file_extension = file_name[file_name.rfind('.'):]

    # Output the corresponding media type or default to 'application/octet-stream'
    print(media_types.get(file_extension, 'application/octet-stream'))

if __name__ == "__main__":
    main()
