def main():
    event_name = get_event_name()
    event_date = get_event_date()
    event_capacity = get_event_capacity()
    print(f"Event '{event_name}' is scheduled for {event_date} and has a capacity of {event_capacity} people.")

def get_event_name():
    while True:
        name = input("Enter the name of the event: ")
        if len(name) > 0:
            return name
        print("Please enter a valid name for the event.")

def get_event_date():
    while True:
        date = input("Enter the date of the event (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("Please enter a valid date in the format YYYY-MM-DD.")

def get_event_capacity():
    while True:
        capacity = input("Enter the capacity of the event: ")
        if capacity.isdigit() and int(capacity) > 0:
            return capacity
        print("Please enter a valid capacity as a positive integer.")

if __name__ == "__main__":
    main()