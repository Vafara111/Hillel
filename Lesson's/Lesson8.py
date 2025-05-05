# def process_string(text: str) -> str | None:
#     return None
#
# def test_func1(*args):
#     for arg in args:
#         print(arg)
#
# test_func1("1","2","3")
#
# def test_func2(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
#
# test_func2(arg1="1",arg2="2",arg3="3")
#
# def test_func(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
# t = ("1","2","3")
# test_func(*t)
#
# d = {"arg1" : "1","arg2" : "2","arg3" : "3"}
# test_func(**d)
#
# def test_func(func: callable, number):
#     return func(number)
#
# def double(a):
#     """
#         Функція повертає данне число помножене на 2
#         :param a: Дане число, що множиться на 2
#         :return: Результат множення данного числа на 2
#     """
#     return a * 2
#
# print(test_func(double, 2))
#
# def outer():
#     def inner():
#         return "123"
#     return inner
#
# print(outer()())
# print(outer())
# inner_func = outer()
#
# def outer():
#     def inner():
#         return "123"
#     return inner()
#
# print(outer())
#
#
# def factorial(number: int):
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return factorial(number - 1) * number
#
# print(factorial(9))
#
# double = lambda x: x * 2
#
# print(double(2))
#
# map, filter, zip
#
# lst = [1, 2, 3, 4, 5, 6]
# sq_number = map(lambda x: x ** 2, lst)
# print(list(sq_number))
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# filtered = filter(lambda x: True if x % 2 == 0 else False, lst)
# print(list(filtered))
#
ages = [0, 10, 20]
names = ["A", "B", "V"]
height = [181, 179]
zipped = zip(ages, names, height)
print(list(zipped))