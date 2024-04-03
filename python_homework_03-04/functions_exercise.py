import math

#21
# start_range = int(input("Please enter a number to start the range: "))
# end_range = int(input("Please enter a number to end the range: "))

def check_range_numbers(start_range:int,end_range:int):
    for number in range(start_range,end_range):
        if number % 2 == 0:
            if number %6 !=0:
                print("The following numbers is divided by 2 and not a multiple of 6:\n",number)


# check_range_numbers(start_range,end_range +1)
                
#22

ls = [1,2,3,3,3,1,4,5,6,7,9,8,9,7,1,2,10,11,15]

def check_sequance(ls:list):
    dict_of_numbers = {}
    for item in ls:
        if item not in dict_of_numbers:
            dict_of_numbers[item] = 0
        if item in dict_of_numbers:
            dict_of_numbers[item] += 1
    return dict_of_numbers


# print(check_sequance(ls))

    
#24
def calculate_shape(shape, *args): #taking args here cause shape of items can be multiple values to pass.
    if shape == 'square':
        side = args[0]
        return side * side
    elif shape == 'rectangle':
        length, width = args
        return length * width
    elif shape == 'circle':
        radius = args[0]
        return math.pi * radius * radius
    else:
        return "Unsupported shape"

print(calculate_shape('square', 5))
print(calculate_shape('rectangle', 4, 6))
print(calculate_shape('triangle', 3, 4, 5))



#27
# user_input = input("Enter a sentence: ")
def convert_low_upper(sentence:str):
    new_sentence = ''
    for char in sentence:
        if char == char.lower():
            upper = char.upper()
            new_sentence += upper
        elif char == char.upper():
            lower = char.lower()
            new_sentence += lower

    return new_sentence

# print(convert_low_upper(user_input))

#29.
new_dict = {"erez": ""}

def dict_checker(key_check, new_dict: dict):
    keys = list(new_dict.keys())
    for key in keys:
        if key_check in new_dict:
            print(f"You already have {key_check}, as key in the dict!")
            break
    else:
        new_dict[key_check] = ''
        print(f"{key_check} was added to the dict ")
    return new_dict


# a = dict_checker("erezz", new_dict)
# print(a)
