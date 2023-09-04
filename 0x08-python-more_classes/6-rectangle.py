#!/usr/bin/python3

""" Module of a rectangle class

A rectangle class with attributes width and height
"""


class Rectangle:
    """A rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Returns: None
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Print rectangle using # character"""
        if (self.__height == 0) or (self.__width == 0):
            return ""
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Delete a rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """Return area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return (self.__height * 2) + (self.__width * 2)
