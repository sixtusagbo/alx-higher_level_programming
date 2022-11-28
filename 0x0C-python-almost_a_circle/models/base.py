#!/usr/bin/python3
"""
Module that contains the base class
"""
import json
import os
import csv
import turtle


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

    @classmethod
    def create(cls, **dictionary):
        """ dictionary to instance """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ return a list of instances from file """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as file:
            list_json = file.read()

        list_dict = cls.from_json_string(list_json)
        list_instances = []

        for item in list_dict:
            list_instances.append(cls.create(**item))

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes list of instances to csv file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            fields = ['id', 'width', 'height', 'x', 'y']
        else:
            fields = ['id', 'size', 'x', 'y']

        list_dict = []
        if not list_objs:
            pass
        else:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        with open(filename, "w") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes csv to list of instances """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as file:
            list_dict = list(csv.DictReader(file))

        for dictionary in list_dict:
            for key, value in dictionary.items():
                dictionary[key] = int(value)

        list_instances = []
        for dictionary in list_dict:
            list_instances.append(cls.create(**dictionary))

        return list_instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Let's draw it with turtle and python3-tk """
        screen = turtle.getscreen()
        t = turtle.Turtle()
        turtle.bgcolor("#ccc")
        turtle.title("sixtusagbo - ALX Almost a Circle")
        t.pen(pencolor="blue", pensize=3, speed=1)

        # Draw rectangles
        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.fillcolor("orange")
            t.begin_fill()
            for i in range(1, 5):
                if i % 2 == 0:
                    t.forward(rectangle.height)
                else:
                    t.forward(rectangle.width)
                t.right(90)
            t.end_fill()

        # Draw squares
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.fillcolor("purple")
            t.begin_fill()
            for i in range(1, 5):
                t.forward(square.size)
                t.right(90)
            t.end_fill()

        turtle.mainloop()
