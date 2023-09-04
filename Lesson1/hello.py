# Ask user for their name
name = input("Whats your name? ")

# Remove whitespace from name
name = name.strip()

# capitalize first letter
name = name.capitalize()

# capitalise all words
name = name.title()

# combine calls
name = name.strip().title()

"""
This is a multiline comment
"""

first, last = name.split(" ")

# Say hello to the user
print("hello,", end="")
print(name)
print("hello,", name, sep="o")

# Quotes
print("hello, \"friend\"")
print("hello, 'friend'")

# Str interpolation, fstring
print(f"Hello, {name}") 

print(f"Your first name is {first}")