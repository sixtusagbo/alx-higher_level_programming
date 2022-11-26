#!/usr/bin/python3
"""
Module that contains a class BaseGeometry (based on 5-base_geometry.py)
"""


class BaseGeometry:
    """
    Empty class
    """

    def area(self):
        """
        Area of a geometric shape

        Raises:
            Exception: if it is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that recieves the value property

        Args:
            name: name of the property
            value: value of the property

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than or equal to zero
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
