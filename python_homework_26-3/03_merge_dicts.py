dict1 = {
    'erez':24,
    'tomer':23,
    'tal':20,
}
dict2 = {
    'elik':20,
    'gever':60,
    'ahi':70,
    'erez':50,
}


def dict_merger(dict1:dict,dict2:dict):
    """
    This function gets two dicts and merge them.
    this function overwrite values incase they appear in dict2.
    """
    new_dict = {}
    new_dict = dict1 | dict2 # the "|" is an operator to merge dicts
    return new_dict

result = dict_merger(dict1,dict2)
print("Your merged dict is : ",result)