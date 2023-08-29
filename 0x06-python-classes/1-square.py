#!/usr/bin/python3

"""Square class

A module containing a square class called Square.

"""


class Square:
    """A square class

    Attributes:
        __size (int): size of the square
    """
    __size = 3

    def __init__(self, size):
        """Initialize class with size variable

        Args:
            size (int): size of the square

        Returns:
            None
        """
        self.__size = size
