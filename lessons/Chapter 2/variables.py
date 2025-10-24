# Chapter 2. Variables - Point 1.
message = "Hello, World!"
print(message)

# Chapter 2. Variables - Point 2.
# Modify the variable to change the output
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)

# Chapter 2. Variables - Point 3.
# We're going to create an intentional error to see how Python handles it.
message = "Hello Python Crash Course world!"
# print(messag) # Please uncomment this line to see the error


# Here is the error:
# Traceback (most recent call last):
# File "lessons/chapter2_variables.py", line 15, in <module>
# print(messag)  # Intentional typo to cause an error
# NameError: name 'messag' is not defined. Did you mean: 'message'?