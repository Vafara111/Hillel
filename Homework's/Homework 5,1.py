from keyword import kwlist
elements = r""" !"#$%&'()*+,-./:;<=>?@[\]^`{|}~ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
keywords = kwlist
digits = "0123456789"
name = input("Enter name: ")
result = True

while bool(name):
    x = name.find("_")
    y = name.find("_", x + 1)
    if y - x == 1:
        result = False
        break
    for element in elements:
        if element in name:
            result = False
            break
    if not result: break
    for keyword in keywords:
        if keyword == name:
            result = False
            break
    if not result: break
    for digit in digits:
        if name[0] == digit:
            result = False
            break
    break
else:
    result = False

print(result)