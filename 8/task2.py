def dict_to_list(dictionary):
    listd = []

    for key, value in dictionary.items():
        if isinstance(value, int):
            value *= 2
        listd.append((key, value))

    return listd

dictd = {
    'key1': 1,
    'key2': 2,
    'key3': 3
}

print(dict_to_list(dictd))

# Задача 3

def filter_list(list_so, type_value):
    list_filtered = []

    for element in list_so:
        if isinstance(element, type_value):
            list_filtered.append(element)
    
    return list_filtered

print(filter_list([35, True, 'abc', 10], int))

# Задача 4

while True:
    num_1 = float(input("Введите число типа float (1): "))
    num_2 = float(input("Введите число типа float (2): "))

    if num_2 == 0:
        print("Error")
        continue

    print(num_1/num_2)

    reinput = input("Хотите продолжить? yes/no: ")
    if reinput == 'no':
        break
