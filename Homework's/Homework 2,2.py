user_input = int(input("Enter number: "))

number1, mod1 = divmod(user_input, 10000)
number2, mod2 = divmod(mod1, 1000)
number3, mod3 = divmod(mod2, 100)
number4, number5 = divmod(mod3, 10)
x = number5 * 10000 + number4 * 1000 + number3 * 100 + number2 * 10 + number1

print(x)