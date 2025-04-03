try:
    number1 = float(input("Enter number1: "))
    sign = input("Enter sign: ")
    number2 = float(input("Enter number2: "))

    if sign == "+":
        result = number1 + number2
    elif sign == "-":
        result = number1 - number2
    elif sign == "*":
        result = number1 * number2
    elif sign == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Can't divide by zero"
    else:
        result = "Error"

    print(result)
except Exception:
    print("Error")