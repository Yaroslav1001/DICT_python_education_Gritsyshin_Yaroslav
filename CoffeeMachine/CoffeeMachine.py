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
    global water, milk, coffee_beans, cups
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
    global water, milk, coffee_beans, money, cups
    answer_user = input()
    if answer_user == str(1):
        water -= 250
        coffee_beans -= 16
        cups -= 1
        money += 4
        if enough() is None:
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
        if enough() is None:
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
        if enough() is None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'cappuccino'
    elif answer_user == 'back':
        return 'back'


def fill():
    global water, milk, coffee_beans, money, cups
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
        content2()
        return 'remaining'
    elif action_user == 'exit':
        return 'exit'


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def content2(self):
        print('The coffee machine has:')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.coffee_beans) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print(str(self.money) + ' of money')

    def enough(self):
        global water, milk, coffee_beans, cups
        if self.water < 0:
            return "Sorry, not enough water"
        elif self.milk < 0:
            return "Sorry, not enough milk"
        elif self.coffee_beans < 0:
            return "Sorry, not enough coffee_beans"
        elif self.cups < 0:
            return "Sorry, not enough disposable cups"

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:')
        global water, milk, coffee_beans, money, cups
        answer_user = input()
        if answer_user == str(1):
            self.water -= 250
            self.coffee_beans -= 16
            self.cups -= 1
            money += 4
            if enough(self) == None:
                print('I have enough resources, making you a coffee!')
            else:
                print(enough(self))
            return 'espresso'
        elif answer_user == str(2):
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.cups -= 1
            self.money += 7
            if enough(self) is None:
                print('I have enough resources, making you a coffee!')
            else:
                print(enough(self))
            return 'latte'
        elif answer_user == str(3):
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.cups -= 1
            self.money += 6
            if enough(self) is None:
                print('I have enough resources, making you a coffee!')
            else:
                print(enough(self))
            return 'cappuccino'
        elif answer_user == 'back':
            return 'back'

    def fill(self):
        global water, milk, coffee_beans, money, cups
        print("Write how many ml of water you want to add:")
        add_water = int(input())
        self.water += add_water
        print("Write how many ml of milk you want to add:")
        add_milk = int(input())
        self.milk += add_milk
        print("Write how many grams of coffee beans you want to add:")
        add_coffee_beans = int(input())
        self.coffee_beans += add_coffee_beans
        print("Write how many disposable coffee cups you want to add:")
        add_cups = int(input())
        self.cups += add_cups

    def take(self):
        global money
        print("I gave you " + str(money))
        money = 0

    def action(self):
        print('\nWrite action (buy, fill, take, remaining, exit):')
        action_user = str(input())
        if action_user == 'buy':
            print('')
            objects.buy()
            return 'buy'
        elif action_user == 'fill':
            print('')
            objects.fill()
            return 'fill'
        elif action_user == 'take':
            objects.take()
            return 'take'
        elif action_user == 'remaining':
            print('')
            objects.content2()
            return 'remaining'
        elif action_user == 'exit':
            return 'exit'


objects = CoffeeMachine()

while_action = 0

while while_action != 'exit':
    while_action = action()
