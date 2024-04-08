# Dictionary
dictionary = {}

key_1 = input('wsd: ')
value_1 = input('asd: ')

dictionary[key_1] = value_1

key_2 = input('adf: ')
value_2 = input('dwa: ')

dictionary[key_2] = value_2

key_3 = input('erg: ')
value_3 = input('www: ')

dictionary[key_3] = value_3

print(dictionary)

dictionary.popitem()
dictionary.popitem()

dictionary['list_1'] = [1, 2, 3]
dictionary['list_2'] = [4, 5, 6]

print(dictionary)


# Tuple
tuple_1 = (True, 20, '30', 'Hello!')
tuple_2 = (40, 50)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)