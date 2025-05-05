# def generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# gen = generator()
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# gen_cicle = generator()
# for x in gen_cicle:
#     print(x)
#
# def fibonacci_gen(number: int):
#     a, b = 0, 1
#     count = 0
#     while count < number:
#         yield a
#         a, b = b, a + b
#         count += 1
#
# fibonacci = fibonacci_gen(10)
# for x in fibonacci:
#     print(x)
#
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
#
# closure = outer(5)
# print(closure(6))

def decorator_with_args(log_level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Log level: {log_level} start")
            result = func(*args, **kwargs)
            print(f"Log level: {log_level} end")
            return result
        return wrapper
    return decorator

@decorator_with_args("LOG")
def double1(x):
    return x * 2

@decorator_with_args("WARNING")
def double2(x):
    return x * 2

# double = decorator(double)
print(double1(5))
print(double2(5))
