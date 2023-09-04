#!/usr/bin/python3

"""Square module

    A module containing a class called Square representing a square shape.
"""


class Square:
    """A square class

        A class that defines a square by size.

        Attributes:
            __size (int): size of the square.
            __position (tuple): position of the square.
    """

    __size = 3
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """Initialize class with size variable

        Args:
            size (int): size of the square
            position (tuple): position of the square

        Returns:
            None

        Raises:
            TypeError: if size is not an integer or if position is not a tuple
            ValueError: if size is less than 0
        """
        x, y = position
        if (len(position) != 2 or x < 0 or y < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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
                ValueError: if the `size` is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position of the square

            Args:
                None

            Returns:
                The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

            Args:
                value (tuple): New position of the square

            Returns:
                None

            Raises:
                TypeError: if the `position` is not a tuple of 2 positive
                integers
        """
        x, y = value
        if len(value) != 2 or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Print the square with the character `#`

            Args:
                None

            Returns:
                None
        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
