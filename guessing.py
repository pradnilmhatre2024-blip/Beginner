import random

print("\n=== Number Guessing Game ===")

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.\n")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} → Your guess: "))             
    except ValueError:
        print("Please enter a valid number.")        
        continue

    attempts += 1

    if guess < secret:
        print("Too low! ↑")
    elif guess > secret:
        print("Too high! ↓")
    else:
        print(f"\nCorrect! The number was {secret}.")
        print(f"You got it in {attempts} attempt(s)!")
        break

if attempts == max_attempts and guess != secret:
    print(f"\nGame over! The number was {secret}. Better luck next time!")


