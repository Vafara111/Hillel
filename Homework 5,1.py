# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
from keyword import kwlist
elements = r""" !"#$%&'()*+,-./:;<=>?@[\]^`{|}~ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
keywords = kwlist
digits = "0123456789"
name = "_"
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