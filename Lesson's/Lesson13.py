# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, point: "Point"):
#         return Point(x=self.x + point.x, y=self.y + point.y)
#
#     def __mul__(self, other):
#         pass
#
#     def __len__(self):
#         pass
#
#     def __str__(self):
#         return f"Point with coordinate X: {self.x}, and coordinate Y: {self.y}"
#
#     def __lt__(self, other):
#         pass
#
#     def __le__(self, other):
#         pass
#
#     def __gt__(self, other):
#         pass
#
#     def __ge__(self, other):
#         pass
#
#
# point1 = Point(1, 2)
# point2 = Point(3, 4)
#
# point3 = point1 + point2
#
# print(point3.x)
# print(point3.y)

class NotOddError(Exception):
    pass

def divide(x, y):
    if y % 2 != 0:
        raise NotOddError
    return x / y

while True:
    x = int(input("1: "))
    y = int(input("2: "))
    try:
        result = divide(x, y)
        print(result)
    except ZeroDivisionError:
        print("Zero Division Forbidden")
        continue
    except NotOddError:
        print("Y must be odd")
        continue
    else:
        print("else")
    finally:
        print("finally")