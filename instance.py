# Instance Methods
#Assignment:
#Create a class Dog with instance variables name and breed. 
# Add an instance method bark() 
# that prints a message including the dog's name.


# ✅ Python Code: Class Dog with Instance Method

class Dog:
    def __init__(self,name, breed):
        self.name = name   # Instance variable
        self.breed = breed  # Instance variable

    def bark(self):
        print(f"{self.name} is barking! WOOF WOOF!")

# Create Dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")

# Call the instance method
dog1.bark()
dog2.bark()