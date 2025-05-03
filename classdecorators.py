# 17. Class Decorators
# Assignment:
# Create a class decorator 
# add_greeting that modifies a class to add a greet() method 
# returning "Hello from Decorator!". 
# Apply it to a class Person.

# Define the enhanced class decorator
import cls

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    def print_name(self):
        print(f"My name is {self.name}")

    cls.greet = greet    # Add greet method
    cls.print_name = print_name    # Add print_name method
    return cls

# Apply the decorator to the class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test the enhanced class
p = Person("Zafar")
print(p.greet())          # Output : Hell from Decorator!
p.print_name()            # Output : My name is Zafar
