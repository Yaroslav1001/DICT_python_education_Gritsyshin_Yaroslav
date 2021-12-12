import random

box = []
setr = [[a, b] for a in range(7) for b in range(a, 7)]

while len(box) != 14:
    step = random.choice(setr)
    box.append(step)
    setr.remove(step)
gamer = box[:7]
machine = box[7:]
game = []
minus = -1
add = [a for a in box if a[0] == a[0]]

for a in add:
    if a[0] > minus:
        minus = a[0]
        game = a
if game in gamer:
    gamer.remove(game)
    start = "Computer is about to make a move. Press Enter to continue.."
else:
    machine.remove(game)
    start = "It's your turn to make a move. Enter your command"

score = [game]


def bases():
    print("Stock size:", format(len(setr)))
    print("Computer pieces:", format(len(machine)))
    print("Player pieces", format(gamer))

    if len(score) > 6:
        print("".format(score[:3], "...", score[-3:]))
    else:
        print(format(score))
        for i in range(len(gamer)):
            print("".format(i + 1, gamer[i]))


def machine():
    chance = random.choice(range(-len(machine), len(machine) + 1))
    if chance > 0:
        score.append(machine[chance - 1])
        machine.remove(machine[chance - 1])
    elif chance < 0:
        score.insert(0, machine[-chance - 1])
        machine.remove(machine[-chance - 1])
    else:
        score.append(setr[0])
        setr.pop(0)


def gamer(step1):
    if step1 > 0:
        score.append(gamer[step1 - 1])
        gamer.remove(gamer[step1 - 1])
    elif step1 < 0:
        score.insert(0, gamer[-step1 - 1])
        gamer.remove(gamer[-step1 - 1])
    else:
        score.append(setr[0])
        setr.pop(0)


bases()


while True:

    if start == "Computer is about to make a move. Press Enter to continue...":
        print(input("Status: Computer is about to make a move. Press Enter to continue..."))
        machine()
        status = "It's your turn to make a move. Enter your command"
    else:
        gamer_moving = input("Status: It's your turn to make a move. Enter your command. ")
        try:
            int(gamer_moving)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            if int(gamer_moving) in range(-len(gamer), len(gamer) + 1):
                gamer(int(gamer_moving))
                status = "computer"
            else:
                print("Invalid input. Please try again.")
                continue

    bases()

    if len(machine) == 0:
        print("Status: The game is over. The computer won!")
        break
    elif len(gamer) == 0:
        print("Status: The game is over. You won!")
        print("You have 0 pieces")
        break
    elif score[0][0] == score[-1][-1]:
        count = 0
        for f in range(len(score)):
            for s in score[f]:
                if s == score[0][0]:
                    count += 1
        if count == 8:
            print("Status: The game is over. It's a draw!")

            break
