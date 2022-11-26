#!/usr/bin/python3
"""
Test for Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Suite that tests Rectangle
    """

    def setUp(self):
        """
        Invoked for every test
        """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """
        Create a new instance
        """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_height_type(self):
        """
        Height must be integer
        """
        with self.assertRaises(TypeError):
            new = Rectangle(10, "2")

    def test_width_type(self):
        """
        Width must be integer
        """
        with self.assertRaises(TypeError):
            new = Rectangle("10", 2)

    def test_x_type(self):
        """
        x must be integer
        """
        with self.assertRaises(TypeError):
            new = Rectangle(10, 2)
            new.x = []

    def test_y_type(self):
        """
        y must be integer
        """
        with self.assertRaises(TypeError):
            new = Rectangle(10, 2)
            new.y = {}

    def test_width_size(self):
        """ width must be > 0 """
        with self.assertRaises(ValueError):
            new = Rectangle(10, 2)
            new.width = -5

    def test_height_size(self):
        """ height must be > 0 """
        with self.assertRaises(ValueError):
            new = Rectangle(10, 2)
            new.height = -3

    def test_x_size(self):
        """ x cannot be negative """
        with self.assertRaises(ValueError):
            new = Rectangle(10, 2)
            new.x = -4

    def test_y_size(self):
        """ y must be >= 0 """
        with self.assertRaises(ValueError):
            new = Rectangle(10, 2)
            new.y = -2

    def test_area(self):
        """ area must be correct """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)
