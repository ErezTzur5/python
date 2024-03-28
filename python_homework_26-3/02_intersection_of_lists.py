ls_of_int1 = [1,2,3,4,5,6,7,8,9,10]
ls_of_int2 = [11,12,13,14,15,16,17,5,4,3]


def intersection(ls_of_int1:list,ls_of_int2:list):
    """
    This function gets two lists of integers,checks on all the integers and creates a new list with common integers in the lists that were given.
    this function returns a new list.
    """
    result_list = []
    for integer in ls_of_int1:
        if integer in ls_of_int2:
            result_list.append(integer)
    return result_list


result = intersection(ls_of_int1,ls_of_int2) # result should be list of [3,4,5]

print("Your common integer list is:",result)