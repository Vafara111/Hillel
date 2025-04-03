test_list1 = [1, 2, 3, 4, 5, 6]
test_list2 = [1, 2, 3]
test_list3 = [1, 2, 3, 4, 5]
test_list4 = [1]
test_list5 = []

test_list = test_list5

length = len(test_list)
half_length = int(length / 2) if length % 2 == 0 else int(length / 2) + 1
list1 = test_list[0:half_length]
list2 = test_list[half_length:length]
test_list.clear()
test_list.append(list1)
test_list.append(list2)
print(test_list)