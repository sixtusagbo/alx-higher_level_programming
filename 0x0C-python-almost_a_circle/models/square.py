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
