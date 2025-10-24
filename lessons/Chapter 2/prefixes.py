# Removing Prefixes from Strings
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))  # Output: nostarch.com

# Other way
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)  # Output: nostarch.com