def filter_dict_by_prefix(dictionary, prefix):
    """
    This function takes a dictionary and a keyword perfix and filter's all the items that does not start with the key perfix.
    """
    return {key: value for key, value in dictionary.items() if key.startswith(prefix)}

dictionary_test = {
    'bread': 1,
    'meat': 2,
    'orange': 3,
    'omllet': 4,
    'fish': 5
}


prefix = 'o'
result = filter_dict_by_prefix(dictionary_test, prefix)
print(result)