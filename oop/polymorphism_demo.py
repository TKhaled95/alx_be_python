import math

# Base class - Shape
class Shape:
    def area(self):
        """Method that will be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of a rectangle."""
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of a circle."""
        return math.pi * self.radius ** 2
