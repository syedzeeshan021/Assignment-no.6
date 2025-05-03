# ✅ Python Code: Abstract Class Shape and Concrete Class Rectangle

from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass # Abstract method - must be overridden

# Concrete Subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
# Create a Rectangle object
rect = Rectangle(5,3)

# Call the implemented area method
print("Area of the rectangle:", rect.area())


    
