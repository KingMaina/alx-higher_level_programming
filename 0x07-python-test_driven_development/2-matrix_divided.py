#!/usr/bin/python3

""" Matrix division module

    Functions:
        matrix_divided(matrix, div):
            Divides a 2 dimensional matrix by a positive integer or float
"""


def matrix_divided(matrix, div):
    """"Divide a matrix by a positive integer

        Args:
            matrix (list): A list of lists of integers or floats
            div (int or float): An integer or float

        Returns:
            A new matrix resulting from dividing `matrix` by `div`

        Raises:
            TypeError: div must be a number
            TypeError: Each row of the matrix must have the same size
            ValueError: division by infinity
            ZeroDivisionError: division by zero
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div + 1 == div:
        raise ValueError("division by infinity")
    if type(matrix) is not list:
        raise TypeError(
            """
                matrix must be a matrix (list of lists) of integers/floats
            """)
    if matrix == [] or matrix == [[]]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    row_sizes = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                """matrix must be a matrix (list of lists) of integers/floats
                """)
        if len(row) <= 0:
            raise TypeError(
                """matrix must be a matrix (list of lists) of integers/floats
                """)
        row_sizes.append(len(row))
        if len(row_sizes) > 0 and len(row) != row_sizes[0]:
            raise TypeError(
                """Each row of the matrix must have the same size""")
        for value in row:
            if type(value) not in [int, float]:
                raise TypeError(
                    """matrix must be a matrix
                        (list of lists) of integers/floats
                    """
                )
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(round(value / div, 2))
        new_matrix.append(new_row)
    return new_matrix
