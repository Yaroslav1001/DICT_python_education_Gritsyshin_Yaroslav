while True:
    comrades = int(input("Enter the number of friends joining (including you):"))
    if comrades > 0:
        print("Enter the name of every friend (including you), each on a new line:")
        name = [input() for x in range(comrades)]
        dict = {name[y - 1]: 0 for y in range(1, comrades + 1)}
        print(dict)
        price = int(input("Enter the total amount: "))
        if int(price / comrades) != (price / comrades):
            list_amount = [round((price/ comrades), 2)] * comrades
        else:
            list_amount = [round(price / comrades)] * comrades
        dk = list(dict.keys())
        dk.sort()
        for x in range(len(dk)):
            dict[dk[x]] = list_amount[x]
        print(dict)
    elif comrades < 0:
        print("It can't be!")
        continue
    else:
        print("No one is joining for the party.")
        break
