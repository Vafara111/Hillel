def common_elements() -> set:
    set3 = set(range(0, 100, 3))
    set5 = set(range(0, 100, 5))
    return set3.intersection(set5)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}