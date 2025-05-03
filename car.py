# Python Code: car with Public Variable and Method

# Define the Car class
class Car:
    def __init__(self, brand):
        self.brand = brand # Public variable

    def start(self):   # Public method
        print(f"{self.brand} car is starting... Vroom!")


# Create an instance of Car
my_car = Car("Hyundai")

# Access public variable from outside the class
print("Car brand:", my_car.brand)

# Call public method from outside the class
my_car.start()
