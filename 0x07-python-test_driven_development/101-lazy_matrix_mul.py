#!/usr/bin/python3

import numpy as np

""" Matrix multiplication module using NumPy"""


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices

        Args:
            m_a (list): A list of lists of integers or floats
            m_b (list): A list of lists of integers or floats

        Returns:
            A new matrix resulting from multiplying `m_a` by `m_b`

        Raises:
            TypeError: m_a must be a list
            TypeError: m_b must be a list
            TypeError: m_a must be a list of lists
            TypeError: m_b must be a list of lists
            ValueError: m_a can't be empty
            ValueError: m_b can't be empty
            TypeError: m_a should contain only integers or floats
            TypeError: m_b should contain only integers or floats
            TypeError: each row of m_a must be of the same size
            TypeError: each row of m_b must be of the same size
            ValueError: m_a and m_b can't be multiplied
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for column in row:
            if type(column) not in [int, float]:
                raise TypeError(
                    "m_a should contain only integers or floats"
                )
    for row in m_b:
        for column in row:
            if type(column) not in [int, float]:
                raise TypeError(
                    "m_b should contain only integers or floats"
                )
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = np.matmul(m_a, m_b)
    return new_matrix
