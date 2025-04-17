test_list1 = [0, 1, 7, 2, 4, 8]
test_list2 = [1, 3, 5]
test_list3 = [6]
test_list4 = []

test_list = test_list1
x = 0
for i in test_list[::2]:
    x += i

# for i in range(0, len(test_list), 2):
#     x += test_list[i]

result = 0
if bool(test_list):
    result = x * test_list[-1]
print(result)