from random import choice

print("Welcome To Rock-Paper-Scissors")
while True:
    gamer = input("Select any option\nrock\npaper\nscissors\nexit ").strip().lower()
    machine = choice("rps")
    if gamer == machine:
        print("Draw")
        print("Computer's choice -> ", machine)
    elif gamer == "r" and machine == "s" or gamer == "p" and machine == "r" or gamer == "s" and machine == "p":
        print("Player Wins")
        print("Sorry, but the computer chose another option and failed:", machine)
    else:
        print("Enter another word")
        print("Sorry, but the computer chose another option:", machine)
    if gamer == "exit":
        break
