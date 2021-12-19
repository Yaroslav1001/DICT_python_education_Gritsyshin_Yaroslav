from random import choice

print("Welcome To Rock-Paper-Scissors")
gamer = input("Select any option\nrock\npaper\nscissors ").strip().lower()
computer = choice("rps")
if gamer == computer:
    print("Draw")
    print("Computer's choice -> ", computer)
elif gamer == "r" and computer == "s" or gamer == "p" and computer == "r" or gamer == "s" and computer == "p":
    print("Player Wins")
    print("Sorry, but the computer chose another option and failed:", computer)
else:
    print("Enter another word")
    print("Sorry, but the computer chose another option:", computer)
