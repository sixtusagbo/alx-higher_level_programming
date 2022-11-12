#!/usr/bin/python3
"""Unittest for max_integer(list=[...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_at_the_middle(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-1, -0.5, -0.25]), -0.25)

    def test_singleton_list(self):
        self.assertEqual(max_integer([2]), 2)
