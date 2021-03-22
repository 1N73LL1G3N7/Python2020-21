# Stone Paper Scissor
import random

StPaSc = ["St", "Pa", "Sc"]
print("Welcome to Stone Paper Scissors game...")
print("You will get 1 point for winning, 0.5 points for tie and 0 points for losing")
print("This game will be of 10 chances")

user_points = 0
computer_points = 0
i = 0

while i < 10:
    user_choice = input("Enter St for Stone, Pa for Paper or Sc for Scissor :\n")
    computer_choice = random.choice(StPaSc)
    if user_choice == computer_choice:
        print(f"Game {i + 1}")
        print(f"You :", {user_choice}, "Computer :", {computer_choice})
        print("Game Tied")
        user_points += 0.5
        computer_points += 0.5
        i += 1
    elif user_choice == "St" and computer_choice == "Sc":
        print(f"Game {i + 1}")
        print(f"You :", {user_choice}, "Computer :", {computer_choice})
        print("You Won")
        i += 1
        user_points += 1
    elif user_choice == "St" and computer_choice == "Pa":
        print(f"Game {i + 1}")
        print(f"You :", {user_choice}, "Computer :", {computer_choice})
        print("Computer Won")
        i += 1
        computer_points += 1
    elif user_choice == "Pa" and computer_choice == "St":
        print(f"Game {i + 1}")
        print(f"You :", {user_choice}, "Computer :", {computer_choice})
        print("You Won")
        i += 1
        user_points += 1
    elif user_choice == "Pa" and computer_choice == "Sc":
        print(f"Game {i + 1}")
        print(f"You :", {user_choice}, "Computer :", {computer_choice})
        print("Computer Won")
        i += 1
        computer_points += 1
    elif user_choice == "Sc" and computer_choice == "Pa":
        print(f"Game {i + 1}")
        print(f"You :", {user_choice}, "Computer :", {computer_choice})
        print("You Won")
        i += 1
        user_points += 1
    elif user_choice == "Sc" and computer_choice == "St":
        print(f"Game {i + 1}")
        print(f"You :", {user_choice}, "Computer :", {computer_choice})
        print("Computer Won")
        i += 1
        computer_points += 1
    else:
        print("Invalid input...")

print("Match Over")
print(f"Your Points :", user_points, "VS", "Computer's points :", computer_points)
