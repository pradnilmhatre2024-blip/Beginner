print("=== Personal Info Card ===")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
hobby = input("Enter your hobby: ")
current_year = 2025
birth_year = current_year - age
print(f"\n  Hi {name}! You were born around {birth_year} in {city}.")
print(f"  Someone who loves {hobby} — that's cool!")

