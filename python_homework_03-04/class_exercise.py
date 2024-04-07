########
#  12  #
########

class string_manipulator:
    def __init__(self) -> None:
        pass

    def get_string(self,):
        user_string = input("Please enter an sentance: ")
        return user_string
    
    def print_string(self,user_string:str):
        return user_string.upper()
    
# erez = string_manipulator()
# stringer = erez.get_string()
# print(erez.print_string(stringer))

########
#  11  #
########
    
list_of_numbers = [-25, -10, -7, -3, 2, 4, 8, 10]

class  sum_to_zero:
    def __init__(self,list_of_numbers) -> None:
        self.list_of_numbers = list_of_numbers

    def check_for_elements(self):
        for number in self.list_of_numbers:
            print(number)
        pass

# sum_to_zero(list_of_numbers).check_for_elements()