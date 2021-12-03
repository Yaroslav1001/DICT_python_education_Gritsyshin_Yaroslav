import math
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--annuity", type=float)
parser.add_argument("--type", type=str)
args = parser.parse_args()


def n(principal, payment, interest):
    cal = (interest * 0.01 / 12)
    f = (payment / (payment - cal * principal))
    rn = math.ceil(math.log(f, cal + 1))
    y = rn / 12
    mon = (y - math.floor(y)) * 12
    if math.floor(mon) != 0:
        print(f"It will take {math.floor(y)} years and {math.ceil(mon)} months to repay this loan!\n")
    else:
        print(f"It will take {math.ceil(y)} years to repay this loan!\n")
    print(f"Overpayment {int(principal * (1 + interest * 0.01 / 0.75) - principal)}")


def a(principal, periods, interest):
    cal = (interest * 0.01 / 12)
    num = pow(1 + cal, periods)
    ra = principal * ((cal * num) / (num - 1))
    print(f"Your monthly payment = {math.ceil(ra)}!\n")
    print(f"Overpayment {math.ceil(ra) * periods - principal}")


def p(payment, periods, interest):
    cal = (interest * 0.01 / 12)
    num = pow(1 + cal, periods)
    rp = math.floor(float(payment / ((cal * num) / (num - 1))))
    print(f"Your loan principal = {rp}!\n")
    print(f"Overpayment {payment * periods - rp}")


def diff(principal, periods, interest):
    cal = interest * 0.01 / 12
    mon = 0
    res = 0
    s = list(reversed(range(2, periods + 2)))
    for monthly in s:
        monthly -= 1
        d = math.ceil(principal / periods) + cal * ((principal * monthly) / periods)
        res += d
        mon += 1
        print(f"Month {mon}: payment is {math.ceil(d)}")
    print(f"Overpayment {math.ceil(res - principal)}")


try:
    if args.type == "annuity":
        if args.payment is not None and args.principal is not None:
            if args.principal > 0 and args.payment > 0 and args.interest > 0:
                n(args.principal, args.payment, args.interest)
            else:
                print("Incorrect parameters")
        elif args.principal is not None and args.periods is not None:
            if args.principal > 0 and args.periods > 0 and args.interest > 0:
                a(args.principal, args.periods, args.interest)
            else:
                print("Incorrect parameters")
        elif args.payment is not None:
            if args.payment > 0 and args.periods > 0 and args.interest > 0:
                p(args.payment, args.periods, float(args.interest))
            else:
                print("Incorrect parameters")
    elif args.type == "diff":
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            diff(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
except TypeError:
    print("Incorrect parameters")

