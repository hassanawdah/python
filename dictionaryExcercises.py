def number_square():
    dictionary_1 = {}
    for number in range(1, 16):
        dictionary_1[number] = number ** 2
    print(dictionary_1)


number_square()

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dict1 and dict2 into a new dictionary
merged_dict = {**dict1, **dict2}
merged_dict_1 = dict1 | dict2
print(merged_dict)
print(merged_dict_1)
