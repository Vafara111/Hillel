test_list1 = [0, 1, 0, 12, 3]
test_list2 = [0]
test_list3 = [1, 0, 13, 0, 0, 0, 5]
test_list4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

test_list = test_list4

for i in test_list:
    if i == 0:
        test_list.remove(i)
        test_list.append(i)
print(test_list)