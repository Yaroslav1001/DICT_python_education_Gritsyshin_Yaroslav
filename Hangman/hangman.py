import random

print("HANGMAN\nThe game will be available soon.")

text = ["python", "java", "javascript", "swift"]
while True:
    print("Hangman")
    rand = random.choice(text)
    symb = '-' * len(rand[3:])
    print(rand[:3] + symb)
    gue = input("Guess the word:>")
    if gue == rand:
        print("You survived!")
    else:
        print("You lost!")
