#!/usr/bin/python3

"""Square module

    A module containing a class called Square representing a square shape.
"""


class Square:
    """A class representing a square shape"""

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

    @property
    def size(self):
        """Get the size of the square

            Args:
                None

            Returns:
                The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

            Args:
                value (int): New size of the square

            Returns:
                None

            Raises:
                TypeError: if the `size` is not an integer
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Get the area of the square

            Args:
                None

            Returns:
                The area of the square
        """
        return self.__size ** 2
