#!/usr/bin/python3
"""
Module that contains Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that defines a rectangle that inherits from BaseGeometry Class
    """

    def __init__(self, width, height):
        """
        Initializes instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Implementation of area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        String representation of this object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
