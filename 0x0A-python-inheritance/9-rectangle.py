#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Module containing a Rectangle class"""


class Rectangle(BaseGeometry):
    """An inherited rectangle class"""

    def __init__(self, width, height):
        """Initializes a rectangle class"""
        if self.integer_validator("width", width) is None:
            self.__width = width
        if self.integer_validator("height", height) is None:
            self.__height = height
        BaseGeometry.__init__(self)

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
