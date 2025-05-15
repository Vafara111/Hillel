# def liner(itr, target):
#     for i in range(itr):
#         if itr[i] == target:
#             return i
#     return -1
#
# def binary_search(itr, target):
#     low,high = 0, len(itr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if target == itr[mid]:
#             return mid
#         elif itr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# file = open("text.txt", "r")
# content = file.read()
# print(content)
# file.close()
# file = open("text.txt", "w")
# content = file.write("New test")
# print(content)
# file.close()
# file = open("text.txt", "a")
# content = file.write("\n New test")
# print(content)
# file.close()
#
# with open("text.txt", "r") as file:
#     content = file.read()
#     print(content)

class Car:
    def __init__(self, brand: str):
        self.brand = brand
    def start(self):
        print(f"Starting {self.brand}")
    count_of_wheel = 4


car1 = Car("1")
car2 = Car("2")
print(car1.brand)
print(car2.brand)
car1.start()
car2.start()
