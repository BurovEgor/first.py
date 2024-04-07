listd = ['string', 'lapse', 'pro', 'prolapse', 'api']

list_standard = []

for element in listd:
    if len(element) > 3:
        list_standard.append(element)

list_comprehension = [element for element in listd if len(element) > 3]

print(listd)
print(list_standard)
print(list_comprehension)