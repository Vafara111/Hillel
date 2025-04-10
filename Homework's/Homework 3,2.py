test_list1 = [12, 3, 4, 10]
test_list2 = [1]
test_list3 = []
test_list4 = [12, 3, 4, 10, 8]

test_list = test_list1

print(test_list)
if bool(test_list): test_list.insert(0, test_list.pop(-1))
print(test_list)