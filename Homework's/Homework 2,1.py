user_input = int(input("Enter number: "))
number1, mod1 = divmod(user_input, 1000)
number2, mod2 = divmod(mod1, 100)
number3, number4 = divmod(mod2, 10)

print(number1)
print(number2)
print(number3)
print(number4)