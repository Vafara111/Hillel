def difference(*args: float) -> float:
    numbers = []
    for arg in args:
        numbers.append(arg)
    if numbers:
        minnumber = min(numbers)
        maxnumber = max(numbers)
        return round(maxnumber - minnumber, 2)
    return 0
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2' 
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3' 
assert difference() == 0, 'Test4' 
print('OK')
