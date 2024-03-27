ls = [1,1,1,1,1,2,2,2,3,3,4,4,4,6,7,8]


def freq_of_elements(elements:list):
    """
    This function takes a list and calculate the frequancy of elements in the list.
    this function retuns a dicts of the values.
    """
    result_dict = {}
    for item in elements:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict



result = freq_of_elements(ls)
print(result)