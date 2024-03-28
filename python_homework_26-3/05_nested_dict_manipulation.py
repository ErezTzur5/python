nested_dict = {
    'dict_erez':{'age':'20'},
    'dict_tal':{'age':'19'},
    'dict_tomer':{'age':'18'},
}


def add_key_value_to_dict(nested_dict:dict,key="",value=""):
    """
    This function add value to inner dict.
    this function return dict
    """
    for inner_dict in nested_dict.values():
        # print(inner_dict)
        inner_dict[key] = value
    return nested_dict



result = add_key_value_to_dict(nested_dict,key="City",value="Hadera")
print(result)