print("HANGMAN\nThe game will be available soon.")

while True:
    print("Hangman")
    gue = input("Guess the word:>")
    if gue == "python":
        print("You survived!")
        break
    else:
        print("You lost!")
