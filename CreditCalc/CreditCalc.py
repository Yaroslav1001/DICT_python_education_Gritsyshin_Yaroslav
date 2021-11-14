import math

print("Enter the loan principal:")
lon = int(input("> "))
print("""What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment:""")
w = input()

if w == "p":
        h = int(input("Enter the number of months: \n>"))
        pay = math.ceil(lon /h)
        lp = math.ceil(lon - (h - 1) * pay)
        if lp != pay:
                print("Your monthly payment = {pay} and the last payment = {lp}.")
        else:
                print(f"Your monthly payment = {pay}.")
if w == "m":
        m = int(input("Enter the monthly payment: \n>"))
        payr = lon//m
        print(f"It will take {payr} month to repay the loan. ")