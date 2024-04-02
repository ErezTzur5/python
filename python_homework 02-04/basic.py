import time
import random

#15 Leap Year
def is_leap_year(year):
    """
    This function take's a year as input and checks is the year is leap year or not.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
        return True

    else:
        print(f"{year} is not a leap year.")
        
        return False

# year = int(input("Enter a year: "))
# print(is_leap_year(year))

#16 Random number 1- 100
def guess_it():
    tries = 0
    random_number = random.randint(0, 100)
    print("Random number:", random_number)
    while True:
        tries = tries + 1
        user_number_guess = int(input("Enter a number between 1-100: "))
        if user_number_guess == random_number:
            print("You guessed the right number in", tries, "tries!")
            break
        elif abs(user_number_guess - random_number) <= 10:
            print("Hot")
        else:
            print("Cold")



def counter(seconds):

    count_holder = 0
    while seconds != count_holder:
        print("Mississippi",seconds)
        time.sleep(1)
        seconds = seconds -1

# seconds = int(input("Enter number of seconds you want to count: "))
# counter(seconds)
        

def convert_string(input_string:str):
    converted_string = ""
    for char in input_string:
        if char.isalpha():
            ascii_val = ord(char.lower()) + 2
            if ascii_val > ord('z'):
                ascii_val -= 26
            converted_string += chr(ascii_val)
        else:
            converted_string += char
    return converted_string

# input_string = input("Enter a string: ")
# converted_string = convert_string(input_string)
# print("Converted string:", converted_string)

