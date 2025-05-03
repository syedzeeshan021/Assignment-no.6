# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

# ✅ Python Code: Diamond Inheritance with MRO

# Base class A

class A:
    def show(self):
        print("Show method from Class A")

# Class B inherits from A and overrides show()

class B(A):
    def show(self):
        print("Show method from Class B")

# Class C inherits from A and overrides show()

class C(A):
    def show(self):
        print("Show method from Class C")

# Class D inherits from both B and C

class D(B, C):
    pass   # No override here to observe MRO

# Create an object of D and call show()

obj = D()
obj.show()

# Display Method Resolution Order
print("\nMethod Resolution Order (MRO):")
for cls in D.__mro__:
    print(cls.__name__)


# 🔍 Explanation:
# Even though both B and C override show(), class D(B, C) follows the MRO from left to right.

# So when obj.show() is called:

# Python first looks in D, then B, then C, and finally A.

# B's show() is found first and used.