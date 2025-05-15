def pow(x):
    return x ** 2

def some_gen(begin: int, end: int, func: callable) -> int:
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    number = begin
    count = 0
    while count < end:
        yield number
        number = func(number)
        count += 1
from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
