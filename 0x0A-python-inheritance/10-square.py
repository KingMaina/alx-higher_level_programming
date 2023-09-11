#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""Module containing a Rectangle class"""


class Square(Rectangle):
    """An inherited square class"""

    def __init__(self, size):
        """Initializes a square class"""
        if self.integer_validator("size", size) is None:
            self.__size = size
        Rectangle.__init__(self)

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Defines the string representation of the square class

            Args:
                None

            Returns:
                The string representation of the class
        """
        return "[Rectangle] {0}/{0}".format(self.__size)
