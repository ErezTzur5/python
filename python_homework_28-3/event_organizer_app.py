
events = {}
# Functions
def my_decorator(func):
    def wrapper():
        print("Welcome to the Event Organizer App!")
        func()
    return wrapper

@my_decorator
def run():
    while True:
        start = input("""Enter 'exit' to exit the program or anything else to continue:
""")
        if start.lower() == 'exit':
                break
        user_date_input = input("""Enter the date of your event in the following format
    `DD-MM-YYYY HH:MM`:\n""") # 27-07-1999 12:15 copy paste to input
        if user_date_input:
            format_checker = formatter(user_date_input)
            if format_checker is True:
                user_event_name_input = input("""Please enter event name:\n""")
                user_location_name_input = input("""Please enter event location name:\n""")
                events[user_event_name_input] = {
                    "event_location": user_location_name_input,
                    "event_date": user_date_input
                }
                print(events)
                add_attendee_names = add_attendee()
                print("Final list of attendees:", add_attendee_names)

                # Scheduling conflict checker
                for event_name, event_details in events.items():
                    if event_name != user_event_name_input:
                        other_event_date = event_details.get("event_date")
                        if other_event_date == user_date_input:
                            print(f"Scheduling conflict: The event {event_name} coincides with another event at the same date and time.")
                            break
                else:
                    print("No scheduling conflict.")




def formatter(data:str):
    """
    This func split the string into parts then it checks if there are exactly two parts, its split the date part into day, month and year.
    """

    parts = data.split(' ')
    

    if len(parts) == 2:
        date_part, time_part = parts
        
        date_parts = date_part.split('-')
        
        if len(date_parts) == 3:
            day, month, year = date_parts

            time_parts = time_part.split(':')
            

            if len(time_parts) == 2:
                hour, minute = time_parts
                
                # Check if all parts are digits
                if day.isdigit() and month.isdigit() and year.isdigit() and hour.isdigit() and minute.isdigit() and len(data)== 16:
                    print("You entered the date in the right format")
                    return True
                else:
                    print("Make sure to add the date in the right format")
                    return False
    else:
        print("Make sure to add the date in the right format")
        return False


def add_attendee(attendee_list: list = []):
    """
    This function gets a list by default and lets you add, remove, and search for participants in an event where the limit is 50.
    This function returns a list of all the participants.

    """
    while len(attendee_list) < 50:
        action = input(
            "Enter 'add' to add an attendee, 'remove' to remove an attendee, 'search' to search for an attendee, or 'done' to finish: ")
        if action.lower() == 'done':
            return attendee_list
        elif action.lower() == 'add':
            name = input("Enter attendee name: ")
            attendee_list.append(name)
            print("Current list of attendees:", attendee_list)
        elif action.lower() == 'remove':
            name = input("Enter attendee name to remove: ")
            if name in attendee_list:
                attendee_list.remove(name)
                print("Removed", name)
                print("Current list of attendees:", attendee_list)
            else:
                print(name, "not found in the list of attendees.")
        elif action.lower() == 'search':
            name = input("Enter attendee name to search: ")
            if name in attendee_list:
                print(name, "is attending the event.")
            else:
                print(name, "is not attending the event.")
        else:
            print("Invalid action. Please enter 'add', 'remove', 'search', or 'done'.")

    if len(attendee_list) == 50:
        print("The maximum limit of 50 attendees has been reached.")


# Main
run()
