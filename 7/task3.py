def route_info(dictionary):
    if ('distance' in dictionary and 
        isinstance(dictionary['distance'], int)):

        return f"Distance to your destination is {dictionary['distance']}"
    
    elif ('speed' and 'time' in dictionary and 
        isinstance(dictionary['speed'], int) and 
        isinstance(dictionary['time'], int)):

        distance = dictionary['speed'] * dictionary['time']
        return f"Distance to your destination is {distance}"
    
    else:
        return "No distance info is available"  

dict_no_values = {}

dict_no_distance = {
    'speed': 2,
    'time': 3
}

dict_distance = {
    'distance': 50
}

print(route_info(dict_no_values))
print(route_info(dict_no_distance))
print(route_info(dict_distance))