#!/usr/bin/python3
"""
Module that contains tests for Base class
"""
import unittest
from models.base import Base


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
