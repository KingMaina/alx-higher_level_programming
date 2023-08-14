#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            print("{:d}".format(matrix[row][col]), end=" ")
        print()
