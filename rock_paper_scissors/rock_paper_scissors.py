from random import choice

print("Welcome To rock-paper-scissors")
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
panel = {}


def gamer_vic(gamer_word, machine_word):
    victory = True
    for word in selection[gamer_word]:
        if word == machine_word:
            victory = False
    return victory


while True:
    try:
        player_name = input("Enter player name: ")  # New gamer
        if player_name not in panel:
            panel[player_name] = 0
        gamer_input = input(                    # Gamer name
            "Select any option"
            "- rock\n"
            "- paper\n"
            "- scissors\n"
            "- gun\n"
            "- lightning\n"
            "- devil\n"
            "- dragon\n"
            "- water\n"
            "- air\n"
            "- sponge\n"
            "- wolf\n"
            "- tree\n"
            "- human\n"
            "- snake\n"
            "- fire\n"
            "- exit\n"
        ).strip()
        machine_input = choice(
            ['rock', 'paper', 'scissors', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'sponge', 'wolf',
             'tree',
             'human', 'snake', 'fire'])
        if gamer_input == machine_input:
            panel[player_name] += 50
            print("Draw")
            print("Computer's choice: ", machine_input)
            print(panel)
        elif gamer_vic(gamer_input, machine_input):
            panel[player_name] += 100
            print("Player Wins")
            print("Computer chose: ", machine_input)
            print(panel)
        elif not gamer_vic(gamer_input, machine_input):
            print("Computer Wins")
            print("Computer chose: ", machine_input)
            print(panel)
        else:
            print("Enter another word")
            print("Sorry, but the computer chose another option:", machine_input)
        if gamer_input == "exit":
            break
    except:
        print("Error: incorrect word. Try once more")
