import random

print("HANGMAN\nThe game will be available soon.")

text = ["python", "java", "javascript", "C#"]
while True:
    print("Hangman")
    gue = input("Guess the word:>")
    if gue == (random.choice(text)):
        print("You survived!")
        break
    else:
        print(random.choice(text))
        print("You lost!")
