#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
"""


class Rectangle:
    """
    Defines a rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializer or class constructor
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Nice string representation
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += "#" * self.width + "\n"

        return string[:-1]

    def __repr__(self):
        """
        Official string representation
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Called when the instance is about to be deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
