#!/usr/bin/python3
""" Module that defines the class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Class constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for attr_item in range(len(attrs)):
                for obj_item in obj:
                    if attrs[attr_item] == obj_item:
                        d_list[obj_item] = obj[obj_item]
            return d_list

        return obj

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for attribute in json:
            self.__dict__[attribute] = json[attribute]
