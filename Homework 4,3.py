import random
i = 0
test_list = []

while i < random.randint(3, 10):
    test_list.append(random.randint(0, 10))
    i += 1
print(test_list)

new_list = [test_list[0], test_list[2], test_list[-2]]
print(new_list)