# This program combines a first and last name into a full name using an "f-string"
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())  # Output: Ada Lovelace

print(f"Hello, {full_name.title()}!")  # Output: Hello, Ada Lovelace!

# Alternatively, storing the name in a variable before using it in the f-string
message = f"Hello, {full_name.title()}!"
print(message)  # Output: Hello, Ada Lovelace!