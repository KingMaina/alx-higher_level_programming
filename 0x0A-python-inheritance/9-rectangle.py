#!/usr/bin/python3

"""Module containing a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """An inherited rectangle class"""

    def __init__(self, width, height):
        """Initializes a rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the shape"""
        return self.__width * self.__height

    def __str__(self):
        """Defines the string representation of the rectangle class

            Args:
                None

            Returns:
                The string representation of the class
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
