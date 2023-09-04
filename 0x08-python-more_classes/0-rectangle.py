#!/usr/bin/python3
"""Defines a Rectangle class."""
class Rectangle:
    """
    This class defines a basic rectangle.
    A rectangle is characterized by its width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with the given width and height.
        
        Args:
            width (float or int): The width of the rectangle.
            height (float or int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.
        
        Returns:
            float or int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.
        
        Returns:
            float or int: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def is_square(self):
        """
        Checks if the rectangle is a square (has equal width and height).
        
        Returns:
            bool: True if the rectangle is a square, False otherwise.
        """
        return self.width == self.height
