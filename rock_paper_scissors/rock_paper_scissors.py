from random import choice

print("Welcome To Rock-Paper-Scissors")
selection = {
    'rock': ['gun', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['fire', 'scissors', 'wolf', 'tree', 'human', 'snake'],
    'scissors': ['gun', 'lightning', 'devil', 'dragon', 'water', 'rock'],
    'gun': ['water', 'air', 'sponge', 'paper', 'devil', 'dragon'],
    'lightning': ['water', 'air', 'sponge', 'paper', 'dragon', 'wolf'],
    'devil': ['water', 'air', 'sponge', 'paper', 'tree', 'wolf'],
    'dragon': ['air', 'sponge', 'paper', 'tree', 'wolf', 'human'],
    'water': ['snake', 'sponge', 'paper', 'tree', 'wolf', 'human'],
    'air': ['snake', 'sponge', 'scissors', 'tree', 'wolf', 'human'],
    'sponge': ['snake', 'scissors', 'tree', 'human', 'rock', 'fire'],
    'wolf': ['snake', 'scissors', 'human', 'rock', 'fire', 'gun'],
    'tree': ['snake', 'scissors', 'rock', 'fire', 'gun', 'lightning'],
    'human': ['scissors', 'rock', 'fire', 'gun', 'lightning', 'devil'],
    'snake': ['rock', 'fire', 'gun', 'lightning', 'devil', 'dragon'],
    'fire': ['fire', 'gun', 'lightning', 'devil', 'dragon', 'water'],
}


def is_player_won(gamer_word, machine_word):
    victory = True
    for word in selection[gamer_word]:
        if word == machine_word:
            victory = False
    return victory


while True:
    gamer_input = input(
        "Select any option\nrock\npaper\nscissors\ngun\nlightning\ndevil\ndragon\nwater\nair\nsponge\nwolf\ntree"
        "\nhuman\nsnake\nfire\nexit\n ").strip()
    machine_input = choice(
        ['rock', 'paper', 'scissors', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'sponge', 'wolf', 'tree',
         'human', 'snake', 'fire'])
    if gamer_input == machine_input:
        print("Draw")
        print("Computer's choice -> ", machine_input)
    elif is_player_won(gamer_input, machine_input):
        print("Player Wins")
        print("Computer chose: ", machine_input)
    elif not is_player_won(gamer_input, machine_input):
        print("Computer Wins")
        print("Computer chose: ", machine_input)
    else:
        print("Enter another word")
        print("Sorry, but the computer chose another option:", machine_input)
    if gamer_input == "exit":
        break
