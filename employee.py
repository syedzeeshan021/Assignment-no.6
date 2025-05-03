# ✅ Python Code: Employee with Public, Protected, and Private Variables

class Employee:
    def __init__(self, name,salary, ssn):
        self.name = name    # Public
        self._salary = salary  # Protected
        self.__ssn = ssn      # Private

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")   # Can be accessed within the class

# 🧪 Example Usage: Access from Outside


# Create an Employee object
emp = Employee("Ayesha", 55000, "678-45-9098")

# Access public variable
print("\nAccessing Public Variable:")
print("Name:", emp.name)

# Access protected variable
print("\nAccessing Protected Variable:")
print("Salary (should work, but discouraged):", emp._salary)

# Access private variable (should raise AttributeError)
print("\nAccessing Private Variable:")
try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Error:", e)

# Access private variable using name mangling
print("\nAccessing Private Variable via Name Mangling:")
print("SSN:", emp._Employee__ssn)

# Display all info using class method
print("\nUsing display_info() method:")
emp.display_info()


