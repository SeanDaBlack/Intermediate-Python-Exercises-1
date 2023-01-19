def get_combined_dict(dict1, dict2):
    final_dict = {}
    for key in dict1.keys():
        if key in dict2.keys():
            final_dict.update({key: (dict1.get(key) + dict2.get(key))})

    return final_dict


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
