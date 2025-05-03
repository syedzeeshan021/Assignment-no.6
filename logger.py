# ✅ Python Code: Logger with Constructor and Destructor

class Logger:
    def __init__(self):
        print("Logger initialized. [Constructor called]")

    def __del__(self):
        print("Logger is being destroyed. [Destructor called]")

def create_logger():
    log = Logger()
    print("Logger is doing some work...")

create_logger()

print("Function is done. Logger should be destroyed now.")


# 📌 Key Concepts:
# __init__() is the constructor, called when the object is created.

# __del__() is the destructor, called when the object is deleted or goes out of scope.