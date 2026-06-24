def program_01():
    print("\n=== Program 1: Personal Info Card ===")

    name    = input("Enter your name   : ")
    age     = int(input("Enter your age    : "))
    city    = input("Enter your city   : ")
    hobby   = input("Enter a hobby     : ")

    current_year = 2025
    birth_year   = current_year - age

    print("\n--- Your Info Card ---")
    print(f"  Name       : {name}")
    print(f"  Age        : {age} years old")
    print(f"  Birth Year : {birth_year}")
    print(f"  City       : {city}")
    print(f"  Hobby      : {hobby}")
    print(f"\n  Hi {name}! You were born around {birth_year} in {city}.")
    print(f"  Someone who loves {hobby} — that's cool!")
