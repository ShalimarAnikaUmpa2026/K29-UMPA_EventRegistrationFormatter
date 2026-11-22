# Asking for information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event = input("Enter event title: ")
year = int(input("Enter event year: "))
month = (input("Enter event month: "))
day = int(input("Enter event day: "))

# Displaying output
print("Name: ", first_name)
print("Section: ", section)
print("Event:", event)
print("Event Date:", month, day, ",", year)
print("Registration record created successfully.")