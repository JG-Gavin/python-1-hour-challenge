import random
total_rounds = 0
rounds = 0
wins = 0
computer_wins = 0
current_round = 1
finished = 0

print("===Welcome to the Rock, Paper, Scissors Game!===")
print("--------------------------------")
print("Choose Game Mode:")
print("1. Best of 1")
print("2. Best of 3")
print("3. Best of 5")
print("")

while True:
    choice = input("Choose (1, 2, or 3): ")

    if choice == "1":
        rounds = 1
        break
    elif choice == "2":
        rounds = 3
        break
    elif choice == "3":
        rounds = 5
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        print("")

total_rounds = rounds

print("")
print(f"===Game Start! Best of {rounds} Rounds===")
print("--------------------------------")

while rounds > 0:
    print("Round", current_round)
    current_round += 1
    rounds -= 1
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    
    while True:
        player = input("Your choice: ").lower().strip()

        if player in choices:
            break

        print("Invalid choice. Please enter rock, paper, or scissors.")
        print("")

    print("The Computer chose:", computer)
    print("")

    if player == computer:
        print("It's a tie!")
        print("--------------------------------")

    elif player == "rock" and computer == "scissors":
        print("You win!")
        wins += 1
        print("--------------------------------")

    elif player == "paper" and computer == "rock":
        print("You win!")
        wins += 1
        print("--------------------------------")

    elif player == "scissors" and computer == "paper":
        print("You win!")
        wins += 1
        print("--------------------------------")

    else:
        print("You lose!")
        computer_wins += 1
        print("--------------------------------")

    if wins > total_rounds/2:
        print(f"You won {wins} out of {total_rounds} rounds")
        print("")
        print("You won the game!")
        finished = 1
        break

    elif computer_wins > total_rounds/2:
        print(f"The computer won {computer_wins} out of {total_rounds} rounds")
        print("")
        print("You lost the game!")
        finished = 1
        break

if finished == 0:
    print(f"You won {wins} out of {total_rounds} rounds")
    print("")

    if wins > computer_wins:
        print("You won the game!")
    else:
        print("You lost the game!")
else:
    print("")