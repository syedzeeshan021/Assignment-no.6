# 13. Composition
#Assignment:
# Create a class Engine and a class Car. 
# Use composition by passing an Engine object to the Car class during initialization. 
# Access a method of the Engine class via the Car class.

# ✅ Python Code: Composition Example

# Engine class with a method

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start_engine(self):
        print(f"{self.engine_type} engine started.")

# Car class uses Engine via composition
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine # Composition: Car HAS-A Engine
    
    def start(self):
        print(f"{self.brand} car is starting...")
        self.engine.start_engine() # Calling the Engine method through Car

# Create an Engine object
my_engine = Engine("Turbo Charged 1.5L")

# Pass the Engine object to the Car Constructor
my_car = Car("Toyota", my_engine)

# Start the car (which internally starts the engine)
my_car.start()

              