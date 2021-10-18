print("Hello! My name is Newton\nI was created in 2021")
# выводит текст с приветствием

username = input("Please, remind me your name.\n>")
print("What a great name you have," + username)
# запрашивает имя и выводит текст добавляя к нему имя

print("Let me guess your age.")
print('Enter remainders of dividing your age by 3, 5 and 7.')
rem3 = int(input("remainder3>"))
rem5 = int(input("remainder5>"))
rem7 = int(input("remainder7>"))
# запрашивает 3 числа ( результата деления своего возраста на 3,5,7 )

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 150
print("Your age is", age, "; that's a good time to start programming!")
# считает по формуле ,  выводит текст с результатом расчетов

print("Now I will prove to you that I can count to any number you want.")
x = 0
y = int(input(">"))
while x <= y:
    print(x, "!")
    x += 1
# запрашивает целое число и ведет посчет он 0 до заданного числа
print("Completed, have a nice day!")
