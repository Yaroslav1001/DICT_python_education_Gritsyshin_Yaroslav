a = list('_' * 9)
lim = str('_' * 9)
l_1 = ['|', a[0], a[1], a[2], '|']
l_2 = ['|', a[3], a[4], a[5], '|']
l_3 = ['|', a[6], a[7], a[8], '|']
dig = [int(i) for i in range(1,4)]
s_l = [' ', l_1, l_2, l_3, ' ']
answer_1 = 0
answer_2 = 0
i = 0


def vic():
    res = []
    if a.count("X") - a.count("O") >= 2:
        return "Impossible"
    elif a.count("O") - a.count("X") >= 2:
        return "Impossible"
    if l_1[1] == l_1[2] == l_1[3] != '_':
        res.append(l_1[1])
    if l_2[1] == l_2[2] == l_2[3] != '_':
        res.append(l_2[1])
    if l_3[1] == l_3[2] == l_3[3] != '_':
        res.append(l_3[1])
    if l_1[1] == l_2[1] == l_3[1] != '_':
        res.append(l_1[1])
    if l_1[2] == l_2[2] == l_3[2] != '_':
        res.append(l_1[2])
    if l_1[3] == l_2[3] == l_3[3] != '_':
        res.append(l_1[3])
    if l_1[1] == l_2[2] == l_3[3] != '_':
        res.append(l_1[1])
    if l_1[3] == l_2[2] == l_3[1] != '_':
        res.append(l_1[3])
    if res.count('X') >= 2:
        res.remove('X')
    elif res.count('O') >= 2:
        res.remove('O')
    if len(res) == 1:
        return res[0] + ' wins'
    elif '_' not in a:
        if len(res) == 0:
            return "Draw"
    elif '_' in a:
        if len(res) == 0:
            return "Game not finished"


def grid():
    print(lim)
    print(' '.join(l_1))
    print(' '.join(l_2))
    print(' '.join(l_3))
    print(lim)
    print(vic())


def move():
    cycle = 0
    global l_1, l_2, l_3, answer_1, answer_2, i, a
    while cycle != 1:
        i += 1
        print('Enter the coordinates:')
        try:
            answer_1, answer_2 = input().split(' ')
            answer_1 = int(answer_1)
            answer_2 = int(answer_2)
        except ValueError:
            i -= 1
            print('You should enter numbers!')
            continue
        if answer_1 and answer_2 not in dig:
            print('Coordinates should be from 1 to 3!')
            i -= 1
        elif answer_1 and answer_2 in dig:
            if s_l[answer_1][answer_2] != '_':
                i -= 1
                print('This cell is occupied! Choose another one!')
            else:
                if i % 2 == 1:
                    s_l[int(answer_1)][int(answer_2)] = 'X'
                    if answer_1 == 1:
                        a[answer_2 - answer_1] = 'X'
                    elif answer_1 == 2:
                        a[answer_1 + answer_2] = 'X'
                    else:
                        a[answer_1 + answer_2 + 2] = 'X'
                    cycle = 1
                else:
                    s_l[int(answer_1)][int(answer_2)] = 'O'
                    if answer_1 == 1:
                        a[answer_2 - answer_1] = 'O'
                    elif answer_1 == 2:
                        a[answer_1 + answer_2] = 'O'
                    else:
                        a[answer_1 + answer_2 + 2] = 'O'
                    cycle = 1
    grid()


grid()
while vic() == "Game not finished":
    move()

