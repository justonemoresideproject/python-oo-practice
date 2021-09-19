"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start=100):
        self.start = start
        self.count = -1


    def generate(self):
        self.count+=1
        return self.start + self.count
    
    def reset(self):
        self.count = -1

    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

