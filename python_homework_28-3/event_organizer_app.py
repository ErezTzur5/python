events1 = {
    {"event_name":"name",
    "location_name":"location",
    "date_of_event":"date"}
}

events = {}
# Functions
def my_decorator(func):
    def wrapper():
        print("Welcome to the Event Organizer App!")
        func()
    return wrapper

@my_decorator
def run():
    user_date_input = input("""Enter the date of your event in the following format
`DD-MM-YYYY HH:MM`:\n""") # 27-07-1999 12:15 copy paste to input
    if user_date_input:
        format_checker = formatter(user_date_input)
        if format_checker is True:
            user_event_name_input = input("""Please enter event name:\n""")
            user_location_name_input = input("""Please enter even location name:\n""")
            events["event_name"] = user_event_name_input
            print(events)





def formatter(data:str):
    # Split the string into parts
    parts = data.split(' ')
    

    # Check if there are exactly two parts
    if len(parts) == 2:
        date_part, time_part = parts
        
        
        # Split the date part into day, month, and year
        date_parts = date_part.split('-')
        
        # Check if the date part has three parts
        if len(date_parts) == 3:
            day, month, year = date_parts
            
            # Split the time part into hour and minute
            time_parts = time_part.split(':')
            
            # Check if the time part has two parts
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

# Main
run()
