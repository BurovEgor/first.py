dict_1 = {
    'key1': 1,
    'key2': 2
}

dict_2 = {
    'key1': 1,
    'key2': 2
}

dict_3 = {
    'key1': 1,
    'key2': 2
}

list_dicts = [dict_1, dict_3, dict_3]

un_list_1, un_list_2, un_list_3 = list_dicts

def un_dict(arg_1, arg_2):
    print(arg_1, arg_2)

un_dict(*un_list_1)
un_dict(*un_list_2)
un_dict(*un_list_3)