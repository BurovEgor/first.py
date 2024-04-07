def image_info(spec):
    if 'image_id' not in spec:
        raise TypeError("Отсутствует ключ 'image_title'.")
    if 'image_title' not in spec:
        raise TypeError("Отсутствует ключ 'image_id'.")
    
    return f"Image '{spec['image_title']}' has id {spec['image_id']}"

image_spec = {
    'image_title': 'my cat',
    'image_id': 5136
}

param = {
    'width': 1920,
    'height': 1080
}

try:
    print(image_info(image_spec))
    print(image_info(param))
except TypeError as err:
    print(err)