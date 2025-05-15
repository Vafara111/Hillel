# class Car():
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#     def start_engine(self):
#         print(f"Start for {self.model}")
#
#
# car = Car("Tesla", 2021)
# print(car.model)
# print(car.year)
#
# car.start_engine()
#
# print(car.__dict__)

class A(object):
    def test_func(self):
        print("A test")

class B(A):
    def test_func(self):
        super().test_func()
        print("B test")

class C(A):
    pass

class D(B):
    @classmethod
    def class_method(cls):
        print("Class method")
    @staticmethod
    def static_method():
        print("Static method")
    # def __init__(self, obj):
    #     self.c = obj
    def test_func(self):
        super().test_func()
        print("D test")

# c = C()
# d = D(c)
d = D()
d.test_func()