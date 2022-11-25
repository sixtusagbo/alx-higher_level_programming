#!/usr/bin/python3
"""
Module that contains function that checks if the object is an instance of
a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object inherits directly or indirectly from the class

    Args:
        obj: object
        a_class: class

    Returns:
        bool: True if successful, False otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
