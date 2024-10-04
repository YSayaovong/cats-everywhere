# Exercise Cats Everywhere

# Given the below class:

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# Instantiate three cat objects
cats = [
    Cat("Whiskers", 5),
    Cat("Tom", 7),
    Cat("Fluffy", 3)
]

# Function to find the oldest cat
def find_oldest_cat(cats):
    oldest = max(cats, key=lambda cat: cat.age)
    return oldest

# Print the result
oldest_cat = find_oldest_cat(cats)
print(f"The oldest cat is {oldest_cat.age} years old.")
