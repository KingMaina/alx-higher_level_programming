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
