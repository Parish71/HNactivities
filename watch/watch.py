import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Use regular expression to extract the YouTube URL from src attribute of iframe
    pattern = r'<iframe[^>]*\s+src=["\'](https?://(?:www\.)?(youtube\.com/embed/)([-_\w]+))["\'][^>]*>'
    match = re.search(pattern, s)

    if match:
        video_id = match.group(3)
        return f"https://youtu.be/{video_id}"

    return None

if __name__ == "__main__":
    main()
