#!/usr/bin/python3
"""
Module that contains function that adds new attribute
"""


def add_attribute(obj, name, value):
    """
    Function that adds a new attribute to an object if it's possible

    Args:
        obj: object
        name: attribute name
        value: attribute value

    Raises:
        TypeError: when the attribute can't be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
