#bool(0)
#bool([])
#bool(None)

# x = True
# if 5 > 2 and not 7 == 7 or x == False:
#     print("True")
# elif 10 > 5:
#     print("if")
# else:
#     print("False")

# x = int(input("Number: "))
# result = True if x == 1 else False
# print(result)

# lst = [1,2.1,"3", [1.2, 7]]
# lst.append(8)
# print(lst[-2][1])
# lst.insert(1, 5)
# lst.extend([7,2,0])
# lst.extend("1287")
# lst.append(2.1)
# print(lst)
# lst.remove(2.1)
# print(lst)
# x = lst.pop(1)
# print(x)
# del lst[6]
# print(1 in lst)
# print(len(lst))
# result_lst = lst + [5,59,7]

lst = [0, 1, 2, 3, 4, 5]
sliced = lst[1:4]
print(sliced)
print(lst[1:])
print(lst[:5])
print(lst[::2])
print(lst[:])
print(lst[::-1])
print(lst[::-2])
lst1 = lst.copy() # Ссылка на вложеный список остается такой же
from copy import deepcopy
lst2 = deepcopy(lst) # Отсылает на новый вложеный список