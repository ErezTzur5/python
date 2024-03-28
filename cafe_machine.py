resources = {'Water': 5000, 'Milk': 5000, 'Coffee': 5000, 'Money': 0}
latte = {'Water': 200, 'Milk': 150, 'Coffee': 24, 'Money': 2.5}
espresso = {'Water': 50, 'Milk': 0, 'Coffee': 18, 'Money': 1.5}
cappuccino = {'Water': 100, 'Milk': 5000, 'Coffee': 5000, 'Money': 0}

def greeting(func):
    def wrapper():
        print("Welcome!\n")
        func()
        print("\nGoodbye!")
    return wrapper

@greeting
def run():
    drink = order_drink()
    if drink:
        money = process_coins(drink[1])
        check_for_resources = are_resources_sufficient(resources, drink[0])

def order_drink():
    drink = input("""Please enter a number to choose your drink:
#1.Latte
#2.Espresso
#3.Cappuccino
""")
    if drink == '1':
        return 'latte', 2.5
    elif drink == '2':
        return 'espresso', 1.5
    elif drink == '3':
        return 'cappuccino', 0
    else:
        print("Number invalid please choose a number from 1 to 3")
        return None

def process_coins(price_of_coffee):
    user_money = float(input(f"Please insert {price_of_coffee}$\n"))
    while user_money < price_of_coffee:
        add_more_money = round(price_of_coffee - user_money, 2)
        user_money += float(input(f"Please add {add_more_money}$ to purchase the coffee\n"))
    print(f"Total Money inserted:{user_money}")
    return user_money

def are_resources_sufficient(machine_resources:dict,user_drink:str):
    if user_drink == 'latte': #LATTE

        if machine_resources['Water'] <= latte['Water']:
            print("coffee machine doesnt have enough water for latte")
        else:
            machine_resources['Water'] = machine_resources['Water'] - latte['Water']

        if machine_resources['Milk'] <= latte['Milk']:

            print("coffee machine doesnt have enough milk for latte")
        else:
            machine_resources['Milk'] = machine_resources['Milk'] - latte['Milk']


        if machine_resources['Coffee'] <= latte['Coffee']:

            print("coffee machine doesnt have enough coffee for latte")
        else:
            machine_resources['Coffee'] = machine_resources['Coffee'] - latte['Coffee']
        print(f"""Making latte!\n Your current resources is:{machine_resources}""")

    elif user_drink == 'espresso': #espresso
        if machine_resources['Water'] <= espresso['Water']:
            print("coffee machine doesnt have enough water for espresso")
        else:
            machine_resources['Water'] = machine_resources['Water'] - espresso['Water']

        if machine_resources['Milk'] <= espresso['Milk']:

            print("coffee machine doesnt have enough milk for espresso")
        else:
            machine_resources['Milk'] = machine_resources['Milk'] - espresso['Milk']

        if machine_resources['Coffee'] <= espresso['Coffee']:

            print("coffee machine doesnt have enough coffee for espresso")
        else:
            machine_resources['Coffee'] = machine_resources['Coffee'] - espresso['Coffee']
        print(f"""Making espresso!\n Your current resources is:{machine_resources}""")
        
    elif user_drink == 'cappuccino':#espresso

        if machine_resources['Water'] < cappuccino['Water']:
            print("coffee machine doesnt have enough water for cappuccino")
        else:
            machine_resources['Water'] = machine_resources['Water'] - cappuccino['Water']

        if machine_resources['Milk'] < cappuccino['Milk']:

            print("coffee machine doesnt have enough milk for cappuccino")
        else:
            machine_resources['Milk'] = machine_resources['Milk'] - cappuccino['Milk']

        if machine_resources['Coffee'] < cappuccino['Coffee']:

            print("coffee machine doesnt have enough coffee for cappuccino")
        else:
            machine_resources['Coffee'] = machine_resources['Coffee'] - cappuccino['Coffee']

        print(f"""Making cappuccino!\n Your current resources is:{machine_resources}""")


if __name__ == "__main__":
    run()
