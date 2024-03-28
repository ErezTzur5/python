# Coffee Extra

# Constants
menu = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

resources = {"water": 5000, "milk": 5000, "coffee": 5000, "money": 0.0}

money_options = {
    'p': 0.01,
    'n': 0.05,
    'd': 0.1,
    'q': 0.25
}

# Functions
def my_decorator(func):
    def wrapper():
        print("Welcome!")
        func()
        print("Hope you enjoyed your drink☕,Goodbye! ")
    return wrapper

@my_decorator
def run():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino/off): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            print_report()
        elif choice in menu:
            order_ingredients = menu[choice]["ingredients"]
            if are_resources_sufficient(order_ingredients):
                price = menu[choice]["cost"]
                money_received = process_coins(price)
                if is_transaction_successful(money_received, price):
                    make_coffee(order_ingredients, choice)

def are_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins(price):
    total = 0.0
    while total < price:
        print(f"Please insert coins or click c to cancel: {price - total:.2f} left")
        coin = input("Sensor ([q]quarters/[d]dimes/[n]nickels/[p]pennies): ").lower()
        if coin == 'c':
            return 0
        if coin in money_options:
            total += money_options[coin]
            print(f"{total:.2f} inserted {price - total:.2f} left")
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.") #2f round the float number up to make it two decimal numbers after the dot
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(order_ingredients, drink_name):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name}.")

def print_report():
    print("Water:", resources["water"], "ml")
    print("Milk:", resources["milk"], "ml")
    print("Coffee:", resources["coffee"], "g")
    print("Money: $", resources["money"])

# Main
run()
