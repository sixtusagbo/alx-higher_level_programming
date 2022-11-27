#!/usr/bin/python3
"""
Test for Square class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """
    Suite that tests Square
    """

    def setUp(self):
        """
        Invoked for every test
        """
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """
        Create a new instance
        """
        new = Square(4)
        self.assertEqual(new.size, 4)
        self.assertEqual(new.width, 4)
        self.assertEqual(new.height, 4)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_validate_attrs_0(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_validate_attrs_1(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_validate_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_validate_attrs_0(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(0)

    def test_validate_attrs_1(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, -1)

    def test_validate_attrs_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_square_is_base_instance(self):
        """ Square is Base instance """
        new = Square(3, 4)
        self.assertTrue(isinstance(new, Base))

    def test_square_is_rectangle_instance(self):
        """ Square is Rectangle instance """
        new = Square(3, 4)
        self.assertTrue(isinstance(new, Rectangle))

    def test_area(self):
        """ area must be correct """
        r1 = Square(3)
        r2 = Square(10)
        self.assertEqual(r1.area(), 9)
        self.assertEqual(r2.area(), 100)

    def test_x_and_y_not_part_of_area(self):
        """ x and y are not part of
        the area computation
        """
        r3 = Square(8, 7, 0, 12)
        self.assertEqual(r3.area(), 64)

    def test_display_0(self):
        """ print in stdout with char # """
        r1 = Square(4)
        expected = "####\n####\n####\n####\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_square_str(self):
        """ string representation """
        r1 = Square(4, 6, 2, 12)
        expected = "[Square] (12) 6/2 - 4\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r2 = Square(5, 5, 1)
        expected = "[Square] (1) 5/1 - 5\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r2)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_with_x_and_y(self):
        """ Display with # character taking
        care of x and y
        """
        r1 = Square(2, 2, 2, 2)
        expected = "\n\n  ##\n  ##\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

        r2 = Square(3, 1, 0)
        expected = " ###\n ###\n ###\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_update_with_args(self):
        """ Update the class with args """
        r1 = Square(10, 10, 10, 10)
        expected = "[Square] (10) 10/10 - 10\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(89)
        expected = "[Square] (89) 10/10 - 10\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(89, 2)
        expected = "[Square] (89) 10/10 - 2\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(89, 2, 3)
        expected = "[Square] (89) 3/10 - 2\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(89, 2, 3, 4)
        expected = "[Square] (89) 3/4 - 2\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_update_with_kwargs(self):
        """ Update with kwargs """
        r1 = Square(10, 10, 10, 10)
        expected = "[Square] (10) 10/10 - 10\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(x=12)
        expected = "[Square] (10) 12/10 - 10\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(size=7, y=1)
        expected = "[Square] (10) 12/1 - 7\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)

        r1.update(size=7, id=89, y=3)
        expected = "[Square] (89) 12/3 - 7\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected)
