#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix_divided([[]], 5))
# print(matrix_divided([[2, 6], None], 10))
# print(matrix_divided([[35.654, 23.34, 5]], 5))
print(matrix)
