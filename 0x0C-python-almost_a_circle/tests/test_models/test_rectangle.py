#!/usr/bin/python3
"""
Test for Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
import os


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
            new = Rectangle(10, 2, [])

    def test_y_type(self):
        """
        y must be integer
        """
        with self.assertRaises(TypeError):
            new = Rectangle(10, 2, 3, {})

    def test_width_size_negative(self):
        """ width must be > 0 """
        with self.assertRaises(ValueError):
            new = Rectangle(-5, 2)

    def test_height_size_negative(self):
        """ height must be > 0 """
        with self.assertRaises(ValueError):
            new = Rectangle(10, -3)

    def test_width_size_zero(self):
        """ width must be > 0 """
        with self.assertRaises(ValueError):
            new = Rectangle(0, 2)

    def test_height_size_zero(self):
        """ height must be > 0 """
        with self.assertRaises(ValueError):
            new = Rectangle(10, 0)

    def test_x_size(self):
        """ x cannot be negative """
        with self.assertRaises(ValueError):
            new = Rectangle(10, 2, -4)

    def test_y_size(self):
        """ y must be >= 0 """
        with self.assertRaises(ValueError):
            new = Rectangle(10, 2, 4, -2)

    def test_rectangle_is_base_instance(self):
        """ Rectangle is Base instance """
        new = Rectangle(3, 4)
        self.assertTrue(isinstance(new, Base))

    def test_area(self):
        """ area must be correct """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)

    def test_x_and_y_not_part_of_area(self):
        """ x and y are not part of
        the area computation
        """
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display_0(self):
        """ print in stdout with char # """
        r1 = Rectangle(4, 5)
        expected = "####\n####\n####\n####\n####\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_rectangle_str(self):
        """ string representation """
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r2 = Rectangle(5, 5, 1)
        expected = "[Rectangle] (1) 1/0 - 5/5\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r2)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_with_x_and_y(self):
        """ Display with # character taking
        care of x and y
        """
        r1 = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

        r2 = Rectangle(3, 2, 1, 0)
        expected = " ###\n ###\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_update_with_args(self):
        """ Update the class with args """
        r1 = Rectangle(10, 10, 10, 10)
        expected = "[Rectangle] (1) 10/10 - 10/10\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(89)
        expected = "[Rectangle] (89) 10/10 - 10/10\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(89, 2)
        expected = "[Rectangle] (89) 10/10 - 2/10\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(89, 2, 3)
        expected = "[Rectangle] (89) 10/10 - 2/3\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(89, 2, 3, 4)
        expected = "[Rectangle] (89) 4/10 - 2/3\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(89, 2, 3, 4, 5)
        expected = "[Rectangle] (89) 4/5 - 2/3\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_update_with_kwargs(self):
        """ Update with kwargs """
        r1 = Rectangle(10, 10, 10, 10)
        expected = "[Rectangle] (1) 10/10 - 10/10\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(height=1)
        expected = "[Rectangle] (1) 10/10 - 10/1\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(width=1, x=2)
        expected = "[Rectangle] (1) 2/10 - 1/1\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(y=1, width=2, x=3, id=89)
        expected = "[Rectangle] (89) 3/1 - 2/1\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(x=1, height=2, y=3, width=4)
        expected = "[Rectangle] (89) 1/3 - 4/2\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        r1 = Rectangle(10, 2, 1, 9)
        expected = "[Rectangle] (1) 1/9 - 10/2\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1_dict = r1.to_dictionary()
        expected = "{'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}\n"
        expected += "<class 'dict'>\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1_dict)
            print(type(r1_dict))
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_update_rectangle_with_dictionary(self):
        """ Test update instance with dictionary """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        expected = "[Rectangle] (1) 1/9 - 10/2\nFalse\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r2)
            print(r1 == r2)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_save_to_file_(self):
        """ save none to file """
        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_em_to_file_empty_(self):
        """ save empty to file """
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

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
        json_dictionary = Rectangle.from_json_string("")
        expected = "[]\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(json_dictionary)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_from_json_string_none(self):
        """ convert none to [] """
        json_dictionary = Rectangle.from_json_string(None)
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

    def test_load_from_file_no_file(self):
        """ if the file does not exist """
        try:
            os.remove("Rectangle.json")
        except:
            pass
        list_rect = Rectangle.load_from_file()
        self.assertEqual(list_rect, [])

    def test_load_from_file(self):
        """ load list of instances from file """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rect = Rectangle.load_from_file()
        self.assertTrue(isinstance(list_rect[0], Rectangle))
