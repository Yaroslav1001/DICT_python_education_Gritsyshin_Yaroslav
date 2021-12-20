import random

from typing import Dict

box = []
setr = [[a, b] for a in range(7) for b in range(a, 7)]


while len(box) != 14:
    part = random.choice(setr)
    box.append(part)
    setr.remove(part)
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
    print("If you don't have a suitable dominance press 0 and you get 1 domino.")

    if len(count) > 6:
        print("".format(*count[:3], "...", *count[-3:]))
    else:
        print(format(count))
        for i in range(len(gamer)):
            print("".format(i + 1, gamer[i]))


def machine():

    case = []
    fld = [*count, *machines]
    tet = 0
    score_isp = {a: case[a] for a in range(len(case))}
    get = []
    dict_o = []

    for i in machines:
        if count[0][0] in i or count[-1][1] in i:
            get.append(i)
    if len(get) == 0:
        machines.append(setr[0])
        setr.remove(setr[0])
    else:
        for i in range(len(get)):
            for j in range(len(get[i])):
                tet += score_isp[get[i][j]]
            dict_o.append(tet)
            tet -= tet
        action = {dict_o[i]: i for i in range(len(get))}
        anw = get[action[dict_o[0]]]
        if anw[1] == count[0][0]:
            count.insert(0, anw)
        elif anw[0] == count[0][0]:
            count.insert(0, anw[::-1])
        elif anw[0] == count[-1][1]:
            count.append(anw)
        elif anw[1] == count[-1][1]:
            count.append(anw[::-1])
        machines.remove(anw)

    for i in range(7):
        for b in fld:
            for n in range(len(b)):
                if i == b[n]:
                    tet += 1
        case.append(tet)


base()


while True:

    if start == "Computer is about to make a move. Press Enter to continue...":
        print(input("Status: Computer is about to make a move. Press Enter to continue..."))
        machine()
        status = "It's your turn to make a move. Enter your command"
    else:
        print("Status: It's your turn to make a move. Enter your command.")

        while True:
            gamer_moving = input()
            try:
                int(gamer_moving)
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            else:
                if int(gamer_moving) in range(-len(gamer), len(gamer) + 1):
                    post_gamer = int(gamer_moving)
                    if post_gamer > 0:
                        if gamer[post_gamer - 1][0] == count[-1][1]:
                            count.append(gamer[post_gamer - 1])
                            gamer.remove(gamer[post_gamer - 1])
                        elif gamer[post_gamer - 1][1] == count[-1][1]:
                            count.append(gamer[post_gamer - 1][::-1])
                            gamer.remove(gamer[post_gamer - 1])
                        else:
                            print("Illegal move. Please try again.")
                            continue
                        break
                    elif post_gamer < 0:
                        if gamer[-post_gamer - 1][1] == count[0][0]:
                            count.insert(0, gamer[-post_gamer - 1])
                            gamer.remove(gamer[-post_gamer - 1])
                        elif gamer[-post_gamer - 1][0] == count[0][0]:
                            count.insert(0, gamer[-post_gamer - 1][::-1])
                            gamer.remove(gamer[-post_gamer - 1])
                        else:
                            print("Illegal move. Please try again.")
                            continue
                        break
                    else:
                        gamer.append(setr[0])
                        setr.remove(setr[0])
                        break
                else:
                    print("Invalid input. Please try again.")
                    continue
        start = "computer"

    base()

    if len(machines) == 0:
        print("Status: The game is over. The computer won!")
        break
    elif len(gamer) == 0:
        print("Status: The game is over. You won!")
        print("You have 0 pieces")
        break
    elif count[0][0] == count[-1][-1]:
        score = 0
        for some in range(len(count)):
            for s in count[some]:
                if s == count[0][0]:
                    score += 1
        if score == 8:
            print("Status: The game is over. It's a draw!")
            break
