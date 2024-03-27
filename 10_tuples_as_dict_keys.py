
def tuples_as_dict(x:int,y:int):
    """
    This function gets an X and Y values and returns a dict where the x , y is tuple as the key and value as the sum of the key.
    this function return dictionary
    """
    result_dict = {}
    sum_of_x_y = x + y
    result_dict[x,y] = sum_of_x_y
    return result_dict


result = tuples_as_dict(10,20)

print(result)
