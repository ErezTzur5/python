list_of_tuples = [('A',10),('B',20),('A',7),('C',8),('A',5),('B',30)]



def aggregate_list_values(list_of_tuples:list):
    """
    This Function Checks all the categories and sum on the amount.
    this function returns a dict.
    
    """
    result_dict = {}
    for category , amount in list_of_tuples:
        result_dict[category] = result_dict.get(category,0) + amount # this row checks if the category exist. if so its sum the amount , if not its returns the value as 0 for the category
    
    return result_dict
        

result = aggregate_list_values(list_of_tuples)

print("Your aggregate amount of the categories is :",result)