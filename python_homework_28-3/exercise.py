##Exercise 1 : Absolute Beginner

def check_number(num):
    if num > 0:
        return "Positive number"
    elif num == 0:
        return "Zero"
    else:
        return "Negative number"


num = float(input("Enter a number: "))

result = check_number(num)
print(result)

##Exercise 2 : Absolute Beginner

def check_odd_even(num):
    if num % 2 == 0:
        return "Even number"
    else:
        return "Odd number"


num = int(input("Enter a number: "))

result = check_odd_even(num)
print(result)

##Exercise 3 :  Combining Conditions


def check_positive_divisible_by_5(num):
    if num > 0 and num % 5 == 0:
        return "Positive and divisible by 5"
    else:
        return "Not positive or not divisible by 5"


num = int(input("Enter a number: "))

result = check_positive_divisible_by_5(num)
print(result)

##Exercise 4: Understanding elif

def categorize_number(num):
    if num < 10:
        return "Small"
    elif num <= 100:
        return "Medium"
    else:
        return "Large"


num = int(input("Enter a number: "))

result = categorize_number(num)
print(result)

##Exercise 5: Nested Conditions

def check_character_type(char:str):
    if char.islower():
        return "Lowercase letter"
    elif char.isupper():
        return "Uppercase letter"
    elif char.isdigit():
        return "Digit"
    else:
        return "Other character"

char = input("Enter a character: ")

result = check_character_type(char)
print(result)


##Exercise 6: More on Nesting

def compare_numbers(num1, num2):
    if num1 > num2:
        return "Greater than"
    elif num1 < num2:
        return "Less than"
    else:
        return "Equal to"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = compare_numbers(num1, num2)
print(f"The first number is {result} the second number.")

##Exercise 7: Using Logical Operators

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))


if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

##Exercise 8: Compound Conditions
    
def check_voting_eligibility(age, is_citizen):
    if age >= 18 and is_citizen:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."


age = int(input("Enter your age: "))
is_citizen = input("Are you a citizen? (yes/no): ").lower() == "yes"


result = check_voting_eligibility(age, is_citizen)
print(result)

##Exercise 9: Multi-layered Nesting

def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"


side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))


result = classify_triangle(side1, side2, side3)
print(f"The triangle is classified as: {result}")


##Exercise 10: Comprehensive Application

def calculator(operation, num1, num2):
    if operation == "addition":
        result = num1 + num2
    elif operation == "subtraction":
        result = num1 - num2
    elif operation == "multiplication":
        result = num1 * num2
    elif operation == "division":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operation."

    return f"Result of {operation} is: {result}"


operation = input("Enter the operation (addition, subtraction, multiplication, division): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculator(operation, num1, num2)
print(result)
