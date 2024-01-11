def main():
    dollars = dollars_to_float(input("How much was the meall? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    amount_str = d[1:] # Remove the leading '$' character
    amount_float = float(amount_str) # Convert the amount string to a float
    return amount_float

def percent_to_float(p):
    percent_str = p[:-1] # Remove the trailing '%' character
    percent_float = float(percent_str) / 100 # Convert the percentage string to a float and divide by 100
    return percent_float

main()