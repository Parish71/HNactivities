import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(sys.argv) == 2 or len(sys.argv) > 3:

        print("Invalid usage")
        sys.exit(1)
    elif len(sys.argv) == 3:
        if sys.argv[1] in ['-f', '--font']:
            font = sys.argv[2]
            if font not in figlet.getFonts():
                print("Invalid usage")
                sys.exit(1)
            figlet.setFont(font=font)
        else:
            print("Invalid usage")
            sys.exit(1)
    elif len(sys.argv) == 1:

        figlet.setFont(font=random.choice(figlet.getFonts()))

    text = input("Enter your text: ")

    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
