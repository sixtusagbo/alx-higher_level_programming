#!/usr/bin/python3
"""
Module that contains a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name
"""


class LockedClass:
    """LockedClass
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """Initializes this class
        """
        pass
