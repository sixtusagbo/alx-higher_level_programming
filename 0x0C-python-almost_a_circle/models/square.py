#!/usr/bin/python3
"""
Module that contains Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Inherits from rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Special method for printable string representation """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns argument to each attribute """
        if args is not None and len(args) != 0:
            list_attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if list_attr[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dictionary with object attributes """
        list_attr = ["id", "size", "x", "y"]
        result = {}

        for key in list_attr:
            if key == "size":
                result[key] = getattr(self, "width")
            else:
                result[key] = getattr(self, key)

        return result
