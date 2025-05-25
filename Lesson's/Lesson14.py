# import Test_Module
# from Test_Module import imported_func
# import Lesson's.Test_Module as module
# from Module.First import first_func
# from Module.Second import second_func
# from Module import first_func, second_func
# from Module import *
#
#
# Test_Module.imported_func()
# module.imported_func()
# imported_func()
#
# lst =[1,2,3,4]
# dct = {1:2,3:4}
# print(lst[1]) # __getitem__
# print(dct[1]) # __getitem__
#
# class Car:
#     def __init__(self, name):
#         self.__name = name
#
#     def __getattr__(self, item):
    #     return None
    # def __setattr__(self, key, value):
    #     print("set attr")
    #     self.__dict__[key] = value
        # self.key = value Нескінченна рекурсія
    #
    # def __delattr__(self, item):
    #     print("remove attr")
    #     del self.__dict__[item]
    #
    # name = property()
    #
    # @name.getter
    # @property
    # def name(self):
    #     return self.__name
    # @name.setter
    # def name(self, name):
    #     self.__name = name
    # @name.deleter
    # def name(self):
    #     del self.__name
    #
    # name = property(fget=get_name, fset=set_name, fdel=del_name,doc="Doc")
#
# car = Car("A")
#
# print(car.name) # __getattribute__  __getattr__ __get__
# print(getattr(car, "model", "test"))
# print(hasattr(car, "model"))
# print(hasattr(car, "name"))
# car.model = "B"
# print(car.model)
# setattr(car, "model", "C")


class Coordinate:
    def __init__(self,value):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __del__(self):
        del self.value

Coordinate = property(fset= Coordinate.__set__(),fget=Coordinate.__get__(),fdel=Coordinate.__del__())

class Point:
    x = Coordinate()
    y = Coordinate()

point = Point
print(point.x)
print(point.y)

print(point.x = 10)
print(point.y = 20)