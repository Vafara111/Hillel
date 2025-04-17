# x = ('12"s'
#      '34')
# y = ("12's"
#      "34")
#
# z = """12"s
#     34"""
#
# x = "  I like Python  "
# upper = x.upper()
# print(upper)
#
# lower= x.lower()
# print(lower)
#
# title = x.title()
# print(title)
#
# replace = x.replace("like", "love")
# print(replace)
#
# strip = x.strip() # lstrip(), rstrip()
# print(strip)
#
# split = x.split()
# print(split)
#
# join ="_".join(split)
# print(join)
#
# x = "A AA A"
# print(x.isupper())
# print(x.startswith("A "))
# print(x.endswith(" A"))

name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))

print("Hello, %s %d %.2f>!" % (name, age, height))
print("Hello, {name} your age {age}!".format(name=name, age=age))
print(f"Hello, {name} your age {age}!")

print(ord("A"))
print(ord("А"))
print(chr(65))
print(chr(1040))