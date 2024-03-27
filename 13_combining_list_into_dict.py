def combine_lists_to_dict(keys:list, values:list):
    """
    This functioncombine two lists into a dictionary.

    This function returns a dict: A dictionary where keys are from the 'keys' list and values are from the 'values' list.
    """
    if len(keys) != len(values):
        print("Lists must be of equal length")

    combined_dict = {}
    for index in range(len(keys)):

        combined_dict[keys[index]] = values[index]

    return combined_dict

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

result = combine_lists_to_dict(keys, values)
print(result)