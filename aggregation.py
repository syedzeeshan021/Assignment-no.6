# 14. Aggregation
# Aggregation means a "has-a" relationship 
# where the contained object (like Employee) 
# can exist independently of the container (Department).


# Assignment:
# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store 
# a reference to an Employee object that exists independently of it.

# Here's a clear example of Aggregation in Python 
# using a Department and an Employee class.

# Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")

# Department class (uses aggregation)
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee # Aggregation: refers to an external Employee object

    def show_details(self):
        print(f"\nDepartment: {self.dept_name}")
        print("Assigned Employee:")
        self.employee.display() # Calls the display method of the Employee object

# Create an Employee object (independent)
emp1 = Employee("Raziq Khan", "E001")

# Create a Department and assign the existing employee
dept1 = Department(" IT Department", emp1)

# Show Department Details
dept1.show_details()

# Employee still exists independently
print("\nAccessing employee independently:")
emp1.display()

