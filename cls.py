# Here’s a Python class Counter that uses a class variable and a class method with cls to track how many objects have been created:

class Counter:
    """
    Counter class tracks how many objects have been created.
    Each object has a unique ID and a user-provided name.
    """

    # Class variables
    count = 0 # Tracks total objects
    all_objects = [] # List to store all created objects

    def __init__(self, name):
        self.name = name
        Counter.count += 1
        self.id = Counter.count
        Counter.all_objects.append(self) # Add the object to the list

    @classmethod
    def display_count(cls):
        """ Displays total number of created objects."""
        print(f"Total objects created: {cls.count}")

    @classmethod
    def reset_count(cls):
        """ Resets count and clears the list of objects."""
        cls.count = 0
        cls.all_objects.clear()
        print("\nObject count has been reset and object list cleared.")
    
    def display(self):
        """Display this object's ID and name."""
        print(f"Object ID: {self.id}, Name: {self.name}")

    @classmethod
    def display_all_objects(cls):
        """Display all objects created so far."""
        print("\n--- All Created Objects ---")
        if not cls.all_objects:
            print("No objects to display.")
        else:
            for obj in cls.all_objects:
                obj.display()


def main():
    while True:
        try:
            n = int(input("How many objects do you want to create? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    for i in range(n):
        name = input(f" Enter name for object # {i + 1}: ")
        Counter(name)

    Counter.display_all_objects()
    Counter.display_count()

    # Optionally reset and try again
    choice = input("\nDo you want to reset and create new objects? (yes/no): ").lower()
    if choice == "yes":
        Counter.reset_count()
        main()


# Run the interative program
if __name__ == "__main__":
    main()

