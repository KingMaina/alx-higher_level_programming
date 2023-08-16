#!/usr/bin/python

def square_matrix_simple(matrix=[]):
    if matrix is None:
        return matrix.copy()
    square_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value**2)
        square_matrix.append(new_row)
    return square_matrix
