set_1 = {1, 2, 3, 4}
set_1.add(5)

set_2 = {1, 2, 3, 6, 7, 8}

set_3 = set_1.intersection(set_2)
print(list(set_3))

set_4 = set_1.difference(set_2)
print(list(set_4))