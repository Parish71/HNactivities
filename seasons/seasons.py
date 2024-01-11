from datetime import date, datetime
import inflect
import sys  # Import the sys module

class AgeCalculator:
    def __init__(self):
        self.birthdate = self.get_birthdate_from_user()
        self.engine = inflect.engine()

    def get_birthdate_from_user(self):
        while True:
            try:
                birthdate_str = input("Date of Birth: ")
                birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
                return birthdate
            except ValueError:
                print("Invalid date")
                sys.exit(1)  # Exit the program with an error code

    def calculate_age_in_minutes(self):
        today = date.today()
        birth_datetime = datetime.combine(self.birthdate, datetime.min.time())
        today_datetime = datetime.combine(today, datetime.min.time())
        age_in_minutes = (today_datetime - birth_datetime).total_seconds() / 60
        return round(age_in_minutes)

    def format_number(self, number):
        if number == 0:
            return "Zero"
        else:
            words = self.engine.number_to_words(number, andword="", zero="zero").capitalize()
            return words

    def display_age(self):
        age_in_minutes = self.calculate_age_in_minutes()

        if age_in_minutes == 0:
            print("You were born just now!")
        else:
            formatted_age = self.format_number(age_in_minutes)
            print(f"{formatted_age} minutes")

def main():
    age_calculator = AgeCalculator()
    age_calculator.display_age()

if __name__ == "__main__":
    main()
