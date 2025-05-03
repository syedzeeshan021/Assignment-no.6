# -----------------------------------------
# @property:    Allow access to a method like an attribute
# @<prop>.setter: Sets the value of the property.
# @<prop>.deleter: Deletes the property.
# -----------------------------------------


class Product:
    def __init__(self, price):
        self._price = price    # Private attribute

    # Getter method
    @property
    def price(self):
        return self._price
    
    # Setter method
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    # Deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


# ------------------------------------
# Testing the Product class
# ------------------------------------
p = Product(100)
print(p.price)       # Output: 100

p.price = 150
print(p.price)       # Output: 150

del p.price          # Output: Deleting price...


# Accessing after deletion will raise an AttributeError
# print(p.price)    # Uncommenting this will raise en error

