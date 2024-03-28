def display_item_options():
    user_choice = input("""Please input a number for the desired item to update:
# 1. Food
# 2. Pants
# 3. Shirts
# 4. Toys\n""")

    if user_choice == '1':
        print("You selected Food.")
        user_choice = 'food'
    elif user_choice == '2':
        print("You selected Pants.")
        user_choice = 'pants'
    elif user_choice == '3':
        print("You selected Shirts.")
        user_choice = 'shirts'
    elif user_choice == '4':
        print("You selected Toys.")
        user_choice = 'toys'
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
        user_choice = None
    return user_choice

def select_action(user_choice:str):
    user_select = None
    if user_choice is not None:
        user_select = input("""Please input the number for action:
#1.Add
#2.Remove\n""")
        if user_select == "1":
            print("You chose to Add")
            user_select = 'add'
        elif user_select == "2":
            print("You chose to Remove")
            user_select = 'remove'
        else:
            print("User Didnt choose item for add or remove")
            user_select = None
    else:
        print("")
    return user_select

def update_inventory(user_select:str,user_choice:str,inventory:dict):
    updated_backpack = inventory
    if user_select == "add":
        amount_add = int(input("""Please Input amount of items to add:\n"""))
        updated_backpack[user_choice] += abs(amount_add)

    elif user_select == "remove":
        amount_remove = int(input("""Please Input amount of items to remove:\n"""))
        updated_backpack[user_choice] -= abs(amount_remove)
        if updated_backpack[user_choice] < 0:
            updated_backpack[user_choice] = 0
    return updated_backpack , print(updated_backpack)

def repeat_or_exit():
    modify = input("""Do You want to modify another item?(yes/no)""").lower()
    if modify == "no":
        return modify
    
def main():
    
    backpack = {
        'food': 5,
        'pants':4,
        'shirts':4,
        'toys':4
    }

    while True:
        user_choice_item = display_item_options()
        user_select_action = select_action(user_choice_item)
        updated_backpack = update_inventory(user_select_action,user_choice_item,backpack)
        modify = repeat_or_exit()
        if modify == "no":
            break

if __name__ == "__main__":
    main()
