number = input("Enter number: ")
number = number.replace("-", "")
while True:
    result = 1
    for i in number:
        result *= int(i)
    if result < 10:
        break
    number = str(result)
print(result)