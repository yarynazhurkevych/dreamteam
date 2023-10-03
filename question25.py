def find_common_keys(dict1, dict2):
    common_keys = []

    for key in dict1.keys():
        if key in dict2:
            common_keys.append(key)

    return common_keys


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'a': 5, 'd': 2}

common_keys = find_common_keys(dict1, dict2)

print(f"Common keys: {common_keys}")
