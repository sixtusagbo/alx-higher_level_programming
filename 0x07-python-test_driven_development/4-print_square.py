#!/usr/bin/python3
"""
Module that contains function that prints a square with the character `#`
"""


def print_square(size):
    """Print a square with `#`

    Args:
        size: the length of the square

    Return: nothing

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
