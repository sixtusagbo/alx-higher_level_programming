#!/usr/bin/python3
"""
Module that contains function that checks if two classes are the same instance
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class

    Args:
        obj: an object
        a_class: a class

    Returns: True if the object is exactly an instance of the specified class;
        otherwise False
    """
    return type(obj) is a_class
