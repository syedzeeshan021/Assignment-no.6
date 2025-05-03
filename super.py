# ✅ Python Code: Person and Teacher Classes Using super()

# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f" Person constructor called.Name: {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)   # Call the constructor of the base class
        self.subject = subject
        print(f" Teacher constructor called. Subject: {self.subject}")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")


# 🧪 Example Usage:

# Create a Teacher object
t1 = Teacher("Mr. Ahmed ali", "Physics")

# Display the teacher's info
print("\n --- Teacher Info ---")
t1.display_info()

