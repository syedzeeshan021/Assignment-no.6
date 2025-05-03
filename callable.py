# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor.
#  Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        result = value * self.factor
        print(f"Multipyling {value} by {self.factor} => {result}")
        return result


    
# Create two multiplier instances
m1 = Multiplier(3)
m2 = Multiplier(5)

# Test callability
print(callable(m1))     # Output:True

print(m1(10))           # Output: Multipyling 10 by 3 => 30
print(m2(4))            # Output: Multipyling 4 by 5 => 20

# Chaining: m1(m2(2)) = m1(10) = 30
print(m1(m2(2)))        # Output:
                        # Multipyling 2 by 5 => 10
                        # Multipyling 10 by 3 => 30
