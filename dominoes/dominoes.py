import random


box = []
setr = [[a, b] for a in range(7) for b in range(a, 7)]


while len(box) != 14:
    step = random.choice(setr)
    box.append(step)
    setr.remove(step)
gamer = box[:7]
machines = box[7:]
game = []
minus = -1
give = [a for a in box if a[0] == a[0]]

for a in give:
    if a[0] > minus:
        minus = a[0]
        game = a
if game in gamer:
    gamer.remove(game)
    start = "Computer is about to make a move. Press Enter to continue.."
else:
    machines.remove(game)
    start = "It's your turn to make a move. Enter your command"

count = [game]


def base():
    print("Stock size:", format(len(setr)))
    print("Computer pieces:", format(len(machines)))
    print("Player pieces", format(gamer))
    print("If you don't have a suitable dominance press 0 and you get 1 more.")

    if len(count) > 6:
        print("".format(count[:3], "...", count[-3:]))
    if count == 7:
        print("Game Over")
    else:
        print(format(count))
        for i in range(len(gamer)):
            print("".format(i + 1, gamer[i]))


def machine():
    while True:
        ran = random.choice(range(-len(machines), len(machines) + 1))
        if ran > 0:
            if machines[ran - 1][0] == count[-1][1]:
                count.append(machines[ran - 1])
                machines.remove(machines[ran - 1])
                break
            elif machines[ran - 1][1] == count[-1][1]:
                count.append(machines[ran - 1][::-1])
                machines.remove(machines[ran - 1])
                break
            else:
                continue
        elif ran < 0:
            if machines[-ran - 1][1] == count[0][0]:
                count.insert(0, machines[-ran - 1])
                machines.remove(machines[-ran - 1])
                break
            elif machines[-ran - 1][0] == count[0][0]:
                count.insert(0, machines[-ran - 1][::-1])
                machines.remove(machines[-ran - 1])
                break
            else:
                continue
        else:
            machines.append(setr[0])
            setr.remove(setr[0])
            break


base()


while True:

    if start == "Computer is about to make a move. Press Enter to continue...":
        print(input("Status: Computer is about to make a move. Press Enter to continue..."))
        machines()
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
                rate = int(gamer_moving)
                tries = 3
                if rate > 0:
                    if gamer[rate - 1][0] == count[-1][1]:
                        count.append(gamer[rate - 1])
                        gamer.remove(gamer[rate - 1])
                    elif gamer[rate - 1][1] == count[-1][1]:
                        count.append(gamer[rate - 1][::-1])
                        gamer.remove(gamer[rate - 1])
                    else:
                        print("Illegal move. Please try again.")
                        continue
                elif rate < 0:
                    if gamer[-rate - 1][1] == count[0][0]:
                        count.insert(0, gamer[-rate - 1])
                        gamer.remove(gamer[-rate - 1])
                    elif gamer[-rate - 1][0] == count[0][0]:
                        count.insert(0, gamer[-rate - 1][::-1])
                        gamer.remove(gamer[-rate - 1])
                    else:
                        print("Illegal move. Please try again.")
                        continue
                else:
                    gamer.append(setr[0])
                    setr.remove(setr[0])
                status = "computer"
            else:
                print("Invalid input. Please try again.")
                continue

    base()

    if len(gamer) == 0:
        print("Status: The game is over. The computer won!")
        break
    elif len(gamer) == 0:
        print("Status: The game is over. You won!")
        print("You have 0 pieces")
        break
    elif count[0][0] == count[-1][-1]:
        score = 0
        for bad in range(len(count)):
            for s in count[bad]:
                if s == count[0][0]:
                    score += 1
        if score == 8:
            print("Status: The game is over. It's a draw!")
            break
