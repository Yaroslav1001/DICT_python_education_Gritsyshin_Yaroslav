water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def content2():
    print('The coffee machine has:')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(coffee_beans) + ' of coffee beans')
    print(str(cups) + ' of disposable cups')
    print(str(money) + ' of money')


def enough():
    global water
    global milk
    global coffee_beans
    global money
    if water < 0:
        return "Sorry, not enough water"
    elif milk < 0:
        return "Sorry, not enough milk"
    elif coffee_beans < 0:
        return "Sorry, not enough coffee_beans"
    elif cups < 0:
        return "Sorry, not enough disposable cups"


def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:')
    global water
    global milk
    global coffee_beans
    global money
    global cups
    answer_user = input()
    if answer_user == str(1):
        water -= 250
        coffee_beans -= 16
        cups -= 1
        money += 4
        if enough() == None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'espresso'
    elif answer_user == str(2):
        water -= 350
        milk -= 75
        coffee_beans -= 20
        cups -= 1
        money += 7
        if enough() == None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'latte'
    elif answer_user == str(3):
        water -= 200
        milk -= 100
        coffee_beans -= 12
        cups -= 1
        money += 6
        if enough() == None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'cappuccino'
    elif answer_user == 'back':
        return 'back'


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
    print("I gave you " + str(money))
    money = 0


def action():
    print('\nWrite action (buy, fill, take, remaining, exit):')
    action_user = str(input())
    if action_user == 'buy':
        print("")
        buy()
        return 'buy'
    elif action_user == 'fill':
        print('')
        fill()
        return 'fill'
    elif action_user == 'take':
        take()
        return 'take'
        elif action_user == 'remaining':
        print('')
        remaining()
        return 'remaining'
    elif action_user == 'exit':
        return 'exit'

while_action = 0

while while_action != 'exit':
    while_action = action()