from random import random

p = []
d = [[a, b] for a in range(7) for b in range(7)]

while len(p) != 14:
    part = random.choice(d)
    p.append(part)
    d.remove(part)
gamer = p[:7]
machine = p[7:]
play = []
minus = -1
give = [a for a in p if a[0] == a[0]]

for a in give:
    if a[0] > minus:
        minus = a[0]
        play = a
if play in gamer:
    gamer.remove(play)
    start = "player"
else:
    machine.remove(play)
    start = "computer"

print("Stock pieces: ", format(d))
print("Computer pieces ", format(machine))
print("Player pieces ", format(gamer))
print("Domino snake ", format(play))
print("Status", format(start))
