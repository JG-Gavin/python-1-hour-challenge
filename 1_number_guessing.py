import random

chances = 0
max_number = 0
attempts = 0

print("===Welcome to the Number Guessing Game!===")
print("--------------------------------")
print("1. Easy (5 chances, 1 to 50)")
print("2. Medium (3 chances, 1 to 100)")
print("3. Hard (2 chances, 1 to 100)")
print("4. Insane (1 chance, 1 to 1000)")
print("")

while True:
    choice = input("Difficulty (1-4): ")

    if choice == "1":
        number = random.randint(1, 50)
        chances = 5
        max_number = 50
        break
    elif choice == "2":
        number = random.randint(1, 100)
        chances = 3
        max_number = 100
        break
    elif choice == "3":
        number = random.randint(1, 100)
        chances = 2
        max_number = 100
        break
    elif choice == "4":
        number = random.randint(1, 1000)
        chances = 1
        max_number = 1000
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

print("--------------------------------")
print("You have", chances, "chances to guess the number.")
print("I am thinking of a number between 1 and", max_number, ".")
print("--------------------------------")

while chances > 0:
    chances -= 1
    attempts += 1
    guess = int(input("Your Guess: "))

    if guess < number:
        print(guess, "is too low.")
        print("You have", chances, "chances left")
        print("")
    elif guess > number:
        print(guess, "is too high.")
        print("You have", chances, "chances left")
        print("")
    else:
        print("Correct! You guessed the number in", attempts, "attempts")
        break

if chances == 0:
    print("You lost! The correct answer is,", number)
