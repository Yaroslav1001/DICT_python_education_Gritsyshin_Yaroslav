print('Enter cells:')
a = list(input())


def vic():
    res = []
    if a.count("X") - a.count("O") >= 2:
        return "Impossible"
    elif a.count("O") - a.count("X") >= 2:
        return "Impossible"
    if a[0] == a[1] == a[2] != '_':
        res.append(a[0])
    if a[3] == a[4] == a[5] != '_':
        res.append(a[3])
    if a[6] == a[7] == a[8] != '_':
        res.append(a[6])
    if a[0] == a[3] == a[6] != '_':
        res.append(a[0])
    if a[1] == a[4] == a[7] != '_':
        res.append(a[1])
    if a[2] == a[5] == a[8] != '_':
        res.append(a[2])
    if a[0] == a[4] == a[8] != '_':
        res.append(a[0])
    if a[2] == a[4] == a[6] != '_':
        res.append(a[2])
    if res.count('X') >= 2:
        res.remove('X')
    elif res.count('O') >= 2:
        res.remove('O')
    if len(res) >= 2:
        return "Impossible"
    elif len(res) == 1:
        return res[0] + ' wins'
    elif '_' not in a:
        if len(res) == 0:
            return "Draw"
    elif '_' in a:
        if len(res) == 0:
            return "Game not finished"


def grid():
    print('---------')
    print('| ' + a[0] + ' ' + a[1] + ' ' + a[2] + ' |')
    print('| ' + a[3] + ' ' + a[4] + ' ' + a[5] + ' |')
    print('| ' + a[6] + ' ' + a[7] + ' ' + a[8] + ' |')
    print('---------')
    print(vic())


grid()
