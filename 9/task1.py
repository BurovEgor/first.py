dictionary = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

dictionary_standard = {}

for key, value in dictionary.items():
    dictionary_standard[key] = value.upper()

dictionary_comprehension = {k: v.upper() for k, v in dictionary.items()}

print(dictionary)
print(dictionary_standard)
print(dictionary_comprehension)