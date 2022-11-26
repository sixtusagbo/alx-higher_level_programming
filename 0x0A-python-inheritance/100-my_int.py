#!/usr/bin/python3
"""
Module that contains MyInt class that inherits from int
"""


class MyInt(int):
    """
    Class that inherits from class int
    """

    def __eq__(self, other):
        """
        Method that inverts == check
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        Method that inverts != check
        """
        return int.__eq__(self, other)
