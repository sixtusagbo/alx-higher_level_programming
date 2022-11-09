#!/usr/bin/python3
"""
Module that contains function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrix: list of integers or floats
        div: divisor

    Return:
        A new matrix of results

    Raises:
        TypeError: if:
            - `matrix` is not a list of integers or floats
            - each row of the `matrix` is not of the same size
            - `div` is not a number
        ZeroDivisionError: if `div` is equal to zero
    """

    matrix_type_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not any(isinstance(el, list) for el in matrix):
        raise TypeError(matrix_type_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not len(set(map(len, matrix))) == 1:
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for elems in matrix:
        for num in elems:
            if not isinstance(num, (int, float)):
                raise TypeError(matrix_type_msg)

    return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)),
                    matrix))
