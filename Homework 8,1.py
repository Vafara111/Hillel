def add_one(some_list: list) -> list:
    number = ""
    new_list = []
    for i in some_list:
        number += str(i)
    number = int(number) + 1
    number = list(str(number))
    for i in number:
        new_list.append(int(i))
    return new_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")