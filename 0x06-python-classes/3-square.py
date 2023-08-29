#!/usr/bin/python3

"""Square class

    A module containing a class called Square representing a square shape.
"""


class Square:
    """A class representing a square shape

    Attributes:
        __size (int): size of the square
    """
    __size = 3

    def __init__(self, size=0):
        """Initialize class with size variable

        Args:
            size (int): size of the square

        Returns:
            None

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculate the area of the square

        Args:
            None

        Returns:
            The area of the square
        """
        return self.__size ** 2
