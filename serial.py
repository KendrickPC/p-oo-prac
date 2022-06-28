"""Python serial number generator."""

class SerialGenerator:
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
    def __init__(self, start=100):
        """Make a new generator/ JS Constructor with start default at 100"""
        self.start = start
        self.next = start + 1

    def __repr__(self):
        """Show representation of class when printed"""
        return f"<SerialGenerator start={self.start}>"

    def generate(self):
        """Return next number/int in sequence"""
        self.next += 1
        return self.next-1

    def reset(self):
        self.next = self.start

test = SerialGenerator()
print(test.generate())
print(test.generate())
print(test.generate())
print(test.generate())
print(test.generate())
test.reset()
print(test.generate())