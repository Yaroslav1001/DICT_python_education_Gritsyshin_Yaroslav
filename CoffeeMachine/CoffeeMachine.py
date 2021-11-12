water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def content():
    print('The coffee machine has:')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(coffee_beans) + ' of coffee beans')
    print(str(cups) + ' of disposable cups')
    print(str(money) + ' of money')


content()
print("")


def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    global water
    global milk
    global coffee_beans
    global money
    global cups
    answer_user = int(input())
    if answer_user == 1:
        water -= 250
        coffee_beans -= 16
        cups -= 1
        money += 4
    elif answer_user == 2:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        cups -= 1
        money += 7
    elif answer_user == 3:
        water -= 200
        milk -= 100
        coffee_beans -= 12
        cups -= 1
        money += 6


def fill():
    global water
    global milk
    global coffee_beans
    global money
    global cups
    print("Write how many ml of water you want to add:")
    add_water = int(input())
    water += add_water
    print("Write how many ml of milk you want to add:")
    add_milk = int(input())
    milk += add_milk
    print("Write how many grams of coffee beans you want to add:")
    add_coffee_beans = int(input())
    coffee_beans += add_coffee_beans
    print("Write how many disposable coffee cups you want to add:")
    add_cups = int(input())
    cups += add_cups


def take():
    global money
    print("I gave you " + str(money) + "\n")
    money = 0


def action():
    print('Write action (buy, fill, take):')
    action_user = input()
    if action_user == 'buy':
        buy()
        content()
    elif action_user == 'fill':
        fill()
        content()
    elif action_user == 'take':
        take()
        content()


action()
