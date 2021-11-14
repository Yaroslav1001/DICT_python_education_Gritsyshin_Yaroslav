import math


def n():
    c = int(input("Enter the loan principal:\n"))
    mp = int(input("Enter the monthly payment:\n"))
    li = float(input("Enter the loan interest:\n"))
    cal = (li * 0.01 / 12)
    fraction = (mp / (mp - cal * c))
    result_n = math.ceil(math.log(fraction, cal + 1))
    years = result_n / 12
    month = (years - math.floor(years)) * 12

    if math.floor(years) != 0:
        print(f"It will take {math.floor(years)} years and {math.ceil(month)} months to repay this loan!\n>")
    else:
            print(f"It will take {math.ceil(years)} years to repay this loan!\n")


def a():
    c = int(input("Enter the loan principal:\n"))
    per = int(input("Enter the number of periods:\n"))
    li = float(input("Enter the loan interest:\n"))
    cal = (li * 0.01 / 12)
    num = pow(1 + cal, per)
    ra = c * ((cal * num) / (num - 1))
    print(f"Your monthly payment = {math.ceil(ra)}!\n")


def p():
    ann = float(input("Enter the annuity payment:\n"))
    per = int(input("Enter the number of periods:\n"))
    li = float(input("Enter the loan interest:\n"))
    cal = (li * 0.01 / 12)
    num = pow(1 + cal, per)
    result_p = ann / ((cal * num) / (num - 1))
    print(f"Your loan principal = {math.floor(result_p)}!\n")


while True:
    choice = input(f"""What do you want to calculate?
        type "n" for number of monthly payments,
        type "a" for annuity monthly payment amount,
        type "p" for loan principal:\n >""")
    if choice == "n":
            n()
    if choice == "a":
            a()
    if choice == "p":
            p()
    break

