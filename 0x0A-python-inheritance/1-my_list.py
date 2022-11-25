#!/usr/bin/python3
"""
Module that contains a class `MyList` that inherits from `list`
"""


class MyList(list):
    """
    Class that inherits from `list`

    Args:
        list: Built-in class `list`
    """

    def print_sorted(self):
        list_clone = self[:]
        list_clone.sort()
        print(list_clone)
