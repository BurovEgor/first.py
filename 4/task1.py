list_1 = ['apple', 'banana', 'kiwi']
list_2 = [20, 15, 30]

zip_1 = zip(list_1, list_2)

zip_1 = list(zip_1)
zip_1 = dict(zip_1) 

print(zip_1)


def merge_lists_to_dict(set_1, set_2):
    zip_fn = zip(set_1, set_2)
    zip_fn = dict(zip_fn)
    return zip_fn

result = merge_lists_to_dict(list_1, list_2)

print(result)