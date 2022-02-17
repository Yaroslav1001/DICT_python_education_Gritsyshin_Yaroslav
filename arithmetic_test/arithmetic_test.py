import random

n = 0
coin = 0

while n < 5:
    symbol = ('+', '-', '*')
    rand = random.choice(symbol)
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    print(num1, rand, num2)
    try:
        if rand == '+':
            if int(input(">")) == num1 + num2:
                print("Right!")
            else:
                print("Wrong!")
        elif rand == '-':
            if int(input(">")) == num1 - num2:
                print("Right!")
            else:
                print("Wrong!")
        elif rand == '*':
            if int(input(">")) == num1 * num2:
                print("Right!")
            else:
                print("Wrong!")
        n += 1
        if n == 5:
            print("Your mark is", coin, "/5")
    except ValueError:
        print("Invalid syntax")
