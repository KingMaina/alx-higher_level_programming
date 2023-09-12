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
