list_1 = ['kiwi', 'banana', 'apple']
list_2 = [25, 10, 45]

def merge_lists_to_dict(set_1, set_2):
    zip_fn = zip(set_1, set_2)
    zip_fn = dict(zip_fn)
    return zip_fn

result_1 = merge_lists_to_dict(list_1, list_2)
result_2 = merge_lists_to_dict(list_1, set_2 = list_2)

print(result_1)
print(result_2)


def update_car_info(**args):
    car = args
    car['is_available'] = True

    return car

car_info = update_car_info(brand='Honda', price=37000)

print(car_info)