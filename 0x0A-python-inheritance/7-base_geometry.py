#!/usr/bin/python3

"""Module containing a geometry class"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Throws an `area` exception"""
        raise Exception("area() is not implemented")

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
