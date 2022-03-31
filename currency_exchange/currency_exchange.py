USD = 29.43
EUR = 32.73
UAH = 0.36

print("Американский доллар - 1 mycoin =", USD, "USD\nЕвро - 1 mycoin =", EUR, "EUR\nУкраинская Гривна - 1 mycoin =", UAH, "UAH\n")


user_input = float(input("Please, enter the number of mycoins you have: >"))
print("I will get", round(USD * user_input, 2), "USD from the sale of", user_input, "mycoins")
print("I will get", round(EUR * user_input, 2), "EUR from the sale of", user_input, "mycoins")
print("I will get", round(UAH * user_input, 2), "UAH from the sale of", user_input, "mycoins")