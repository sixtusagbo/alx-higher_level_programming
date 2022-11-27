#!/usr/bin/python3
"""
Module that contains tests for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


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

    def test_save_to_file_none(self):
        """ save json to file """
        Rectangle.save_to_file(None)
        expected = "[]"
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), expected)

    def test_save_to_file(self):
        """ save json to file """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},'
        expected += ' {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), expected)

    def test_from_json_string(self):
        """ convert JSON to list of dictionaries """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        expected = "[{'id': 89, 'width': 10, 'height': 4},"
        expected += " {'id': 7, 'width': 1, 'height': 7}]\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(list_output)
            self.assertEqual(mock_stdout.getvalue(), expected)
        self.assertIs(type(list_output), list)

    def test_from_json_string_empty(self):
        """ convert empty json string to [] """
        json_dictionary = Base.from_json_string("")
        expected = "[]\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(json_dictionary)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_from_json_string_none(self):
        """ convert none to [] """
        json_dictionary = Base.from_json_string(None)
        expected = "[]\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(json_dictionary)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_create(self):
        """ dictionary to instance """
        r1 = Rectangle(3, 5)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
