# Задание 1.

set_1 = {1, 2, 3}
set_2 = {1, 2, 3}

# Результат сравнения выводится в виде bool значения.

print(set_1 == set_2)
# В этом случае происходит сравнение элементов объектов, а не самих объектов. 
# Так как элементы равны друг другу, вывод выдает нам True.

print(set_1 is set_2)
# Тут происходит все наоборот - сравниваются сами объекты, а не то, что внутри.
# Так как объекты разные, вывод выдает нам False.

print(1 in set_1)
# Элемент 1 есть в первом наборе. - True

print(2 not in set_1)
# Элемента 2 нету в первом наборе. - False


# Задача 2.

dict_1 = {
    'brand': 'Honda',
    'price': '37000'
}

dict_2 = {
    'price': '37000',
    'brand': 'Honda'
}

if dict_1 == dict_2:
    print("Dictionary are equal")


# Задача 3.

dict_f = {
    'brand': 'Honda',
    'model': 'Accord',
    'price': '37000'
}

dict_s = {
    'brand': 'Honda',
    'year': '2008',
    'price': '37000'
}

dict_t = {
    'brand': 'Honda',
    'available': 'True',
    'price': '3700'
}

dictionary = dict_f | dict_s | dict_t

print(dictionary)