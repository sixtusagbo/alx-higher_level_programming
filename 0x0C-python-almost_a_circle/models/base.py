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

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string rep to file """
        filename = "{}.json".format(cls.__name__)
        list_dict = []

        if not list_objs:
            pass
        else:
            for item in list_objs:
                list_dict.append(item.to_dictionary())

        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
