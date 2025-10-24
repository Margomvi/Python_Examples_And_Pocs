# This program demonstrates the use of spaces and tabs for formatting output in Python.
print("Python")
print("\tPython")
print("Languages: \nPython \nC \nJavaScript")

# Now we're going to learn how can we delete spaces and tabs
favorite_language = ' Python '
print(favorite_language) # Output will include spaces
print(favorite_language.rstrip()) # Output will remove trailing spaces
print(favorite_language.lstrip()) # Output will remove leading spaces
print(favorite_language.strip()) # Output will remove both leading and trailing spaces
