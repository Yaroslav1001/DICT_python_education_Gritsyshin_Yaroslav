import random

while True:
    comrades = int(input("Enter the number of friends joining (including you):"))
    if comrades > 0:
        print("Enter the name of every friend (including you), each on a new line:")
        name = [input() for x in range(comrades)]
        dict = {name[y - 1]: 0 for y in range(1, comrades + 1)}
        price = int(input("Enter the total amount: "))
        dk = list(dict.keys())
        dk.sort()
        while True:
            choice = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No: ")
            if choice == "Yes":
                pricelist = [round((price / (comrades - 1)), 2)] * comrades
                lucky_friend_index = random.choice(range(comrades))
                lucky_dude = random.choice(range(comrades))
                for x in range(len(dk)):
                    dict[dk[x]] = pricelist[x]
                print(f"{dk[lucky_dude]} is the lucky one!")
                break
            elif choice == "No":
                pricelist = [round((price / comrades), 2)] * comrades
                for x in range(len(dk)):
                    dict[dk[x]] = pricelist[x]
                print("No one is going to be lucky.")
                print(dict)
                break
            else:
                print("Incorrect choice. Try again!")
            break
    elif comrades < 0:
        print("It can't be!")
        continue
    else:
        print("No one is joining for the party.")
        break
