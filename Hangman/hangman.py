from random import choice

print("HANGMAN")

attempt = 8
text = ("python", "java", "javascript", "swift")

rand = choice(text)
symb = '-' * len(rand)
wrong = 0
used = []

while wrong < attempt and symb != rand:
    print('\n', symb)
    guess = input('\nInput a letter: >')
    wrong += 1

    if guess in used:
        print('\n', symb)
        print("\nNo improvements")
        guess = input('input a latter: >')

    used.append(guess)

    if guess in rand:
        new = ''
        for i in range(len(rand)):
            if guess == rand[i]:
                new += guess
            else:
                new += symb[i]
        symb = new
    else:
        print('\nThat letter doesn\'t appear in the word')


if wrong == attempt:
    print('\nYou lost!')

else:
    print("\nThanks for playing! \nWe'll see how well you did in the next stage")
