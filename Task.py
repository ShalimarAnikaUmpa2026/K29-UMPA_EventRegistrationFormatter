# Asking for information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event = input("Enter event title: ")
year = int(input("Enter event year: "))
month = (input("Enter event month: "))
day = int(input("Enter event day: "))

# Formatting information
name = [first_name.strip(), last_name.strip()]
full_name = " " .join(name)
name_code = (full_name.upper())
clean_section = (section.strip().upper())
clean_event = event.strip().title()

# Displaying formatted output
print("Formatted Output:")
print("Name: ", full_name.title())
print("Name Code: ", name_code)
print("Section: ", clean_section)
print("Event:", clean_event)
print("Registration record created successfully.")
