#!/usr/bin/python3
"""
Module that contains tests for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
import os


class TestBase(unittest.TestCase):
    """
    Suite that tests Base class
    """

    def setUp(self):
        """
        Method called for each test
        """
        Base._Base__nb_objects = 0

    def test_without_id(self):
        """
        Without passing id will assign id
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_id(self):
        """
        With passing id will assign id
        """
        b1 = Base(11)
        self.assertEqual(b1.id, 11)

    def test_assign_previous_id_plus_one(self):
        """
        Test if it saves the id
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_string_id(self):
        """
        If id is a string
        """
        b1 = Base("3")
        self.assertEqual(b1.id, "3")

    def test_more_arguments(self):
        """
        More number of arguments supplied
        """
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def test_private_attributes_access(self):
        """
        Cannot access private attribute
        """
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects

    def test_to_json_string(self):
        """ convert list of dictionaries to JSON """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected = "{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}\n"
        expected += "<class 'dict'>\n"
        expected += '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]\n'
        expected += "<class 'str'>\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(dictionary)
            print(type(dictionary))
            print(json_dictionary)
            print(type(json_dictionary))
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_to_json_string_empty(self):
        """ convert empty list to [] """
        json_dictionary = Base.to_json_string([])
        expected = "[]\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(json_dictionary)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_to_json_string_none(self):
        """ convert none to [] """
        json_dictionary = Base.to_json_string(None)
        expected = "[]\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(json_dictionary)
            self.assertEqual(mock_stdout.getvalue(), expected) 
