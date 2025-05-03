# Define a custom exception class named InvalidAgeError
class InvalidAgeError(Exception):
    # Initialize the exception with a default error message
    def __init__(self, message="Age must be 18 or older"):
        super().__init__(message)  # Call the parent Exception constructor with the message

# Define a function to check if age is valid
def check_age(age):
    # If the age is less than 18, raise the custom InvalidAgeError
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")  # Raise custom error with details
    print("Age is valid.")  # If age is valid, print a confirmation message

# Try block to catch exceptions during function execution
try:
    check_age(16)  # Call the function with an invalid age (less than 18)
except InvalidAgeError as e:  # Catch the custom InvalidAgeError if raised
    print("Caught an exception:", e)  # Print the exception message
