#!/usr/bin/python3

""" Module of a rectangle class

A rectangle class with attributes width and height
"""


class Rectangle:
    """A rectangle class

    """

    __height = 0
    __width = 0

    def __init__(self, width=0, height=0):
        """Initialize class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Returns: None
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Get height of the rectangle

        Returns: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of the rectangle

        Args:
            value (int): height of the rectangle

        Returns: None

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get width of the rectangle

        Returns: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the rectangle

        Args:
            value (int): width of the rectangle

        Returns: None

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
