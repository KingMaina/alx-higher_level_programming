#!/usr/bin/python3

def matrix_mul(m_a, m_b):
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
    new_matrix = []
    for row in range(len(m_a)):
        new_matrix.append([])
        for column in range(len(m_b[0])):
            new_matrix[row].append(0)
            for index in range(len(m_b)):
                new_matrix[row][column] += m_a[row][index] * m_b[index][column]
    return new_matrix
