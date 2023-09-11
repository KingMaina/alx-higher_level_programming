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

    def area(self):
        """Calculates the area of the shape"""
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """Validates an integer

            Args:
                name (str): Name representing the integer
                value (int): Integer to be validated

            Returns:
                None

            Raises:
                TypeError: <name> must be an integer
                ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __str__(self):
        """Defines the string representation of the rectangle class

            Args:
                None

            Returns:
                The string representation of the class
        """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width,
                                   self.__height)
