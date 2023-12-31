#!/usr/bin/python3
"""Module containing a Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """An inherited square class"""

    def __init__(self, size):
        """Initializes a square class"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of the sqaure"""
        return self.__size ** 2

    def __str__(self):
        """Defines the string representation of the square class

            Args:
                None

            Returns:
                The string representation of the class
        """
        return "[Square] {0}/{0}".format(self.__size)
