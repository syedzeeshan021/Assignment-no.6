# 16. Function Decorators
# Assignment:
# Write a decorator function 
# log_function_call that prints "Function is being called" 
# before a function executes. 
# Apply it to a function say_hello().


# Define the decorator
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        print(f" Function name: {func.__name__}")
        print(f" Arguments: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Apply the decorator to the function
@log_function_call
def say_hello(name="World"):
    print(f"Hello, {name}!")


# Call the decorator function
say_hello("Akbar")
