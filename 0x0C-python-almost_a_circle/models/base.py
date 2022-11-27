#!/usr/bin/python3
"""
Module that contains the base class
"""
import json


class Base():
    """
    The Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
