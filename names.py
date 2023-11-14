# 7:06:00 Harvard CS50’s Introduction to Programming with Python – Full University Course

names = []

"""
for _ in range(3):
    name = input("What's your name? ")
    print(f"hello, {name}")
"""

"""
for _ in range(3):
    name = input("What's your name? ")
    names.append(name)
"""

# Create a list
for _ in range(3):
    names.append(input("What's your name? "))

# Sort a list
for name in sorted(names):
    print(f"hello, {name}")