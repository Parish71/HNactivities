# Dictionary to associate fruits with their calories
fruit_data = {
    'Apple': 130,
    'Avocado': 50,
    'Banana': 110,
    'Cantaloupe': 50,
    'Grapefruit': 60,
    'Grapes': 90,
    'Honeydew Melon': 50,
    'Kiwifruit': 90,
    'Lemon': 15,
    'Lime': 20,
    'Nectarine': 60,
    'Orange': 80,
    'Peach': 60,
    'Pear': 100,
    'Pineapple': 50,
    'Plums': 70,
    'Strawberries': 50,
    'Sweet Cherries': 100,
    'Tangerine': 50,
    'Watermelon': 80,
}

def main():
    user_input = input("Enter a fruit: ")

    if user_input.title() in fruit_data:
        calories = fruit_data[user_input.title()]
        print(f"Calories: {calories}")
    else:
        print("")

if __name__ == "__main__":
    main()
