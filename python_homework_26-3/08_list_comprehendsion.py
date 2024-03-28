numbers = [1,2,3,4,5,6,7,8,9,10]


def square_of_evens(numbers:list):
    """
    This function takes a list of numbers and squares them , if they even numbers they added to a new list
    """
    result_list = []
    for number in numbers:
        square_number = number**2
        if square_number % 2 == 0:
            result_list.append(square_number)
    return result_list


result = square_of_evens(numbers)
print(result)

            
        
