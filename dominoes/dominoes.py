import random

setr = [[a, b] for a in range(7) for b in range(a, 7)]
box = []


while len(box) != 14:
    step = random.choice(setr)
    box.append(step)
    setr.remove(step)
gamer = box[:7]
machine = box[7:]
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
    machine.remove(game)
    start = "It's your turn to make a move. Enter your command"

print("Stock pieces: ", format(len(setr)))
print("Computer pieces: ", format(len(machine)))
print("Player pieces: ", format(len(gamer)))
print("Domino snake: ", format(game))


for a in range(len(gamer)):
    print(format(a+1),':')
    print(format(gamer[a]))

print("Status", format(start))