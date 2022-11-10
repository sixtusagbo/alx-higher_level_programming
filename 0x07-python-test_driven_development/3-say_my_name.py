#!/usr/bin/python3
"""
Module that contains function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """Says my name

    Args:
        first_name: First name
        last_name: Last name

    Return: My name is <first_name> <last_name>

    Raises:
        TypeError:
            - if `first_name` is not a string
            - if `last_name` is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
