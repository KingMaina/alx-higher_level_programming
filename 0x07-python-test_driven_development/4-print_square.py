#!/usr/bin/python3

"""Square shape module

    Contains functions that make use of
    a square shape

    Functions:
        print_Square(size): Prints
"""


def print_square(size):
    """Prints a square using '#'

        Args:
            size (int): Size of the square

        Returns:
            None

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
            OverflowError: size must be an integer
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print()
