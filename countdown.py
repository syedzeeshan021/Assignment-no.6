# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. 
# Implement __iter__() and __next__() to make the object iterable in a for-loop, 
# counting down to 0.

class Countdown:
    def __init__(self, start):
        # Initialize the countdown with a starting number.
        # 'start' represents the number from which the countdown will begin.
        self.start = start

    def __iter__(self):
        # The __iter__ method is called when an iterator is required for a container.
        # Here, we initialize the current count to the starting number,
        # so that each new iteration starts from the beginning.
        self.current = self.start
        return self  # Return the iterator object (which is the instance itself).

    def __next__(self):
        # The __next__ method returns the next item in the iteration.
        # It is called repeatedly by the iterator protocol.
        if self.current < 0:
            # When the current value falls below 0, we have completed the countdown.
            # Raising StopIteration signals that there are no further items.
            raise StopIteration

        # Save the current number to return it.
        num = self.current
        # Decrement the current value so the next call to __next__ gets the next number.
        self.current -= 1
        # Return the value that was current before decrementing.
        return num

# Example usage of the Countdown class:
if __name__ == "__main__":
    # When iterating over an instance of Countdown starting at 5,
    # the for-loop will sequentially decrease the number until it reaches 0.
    for number in Countdown(5):
        print(number)