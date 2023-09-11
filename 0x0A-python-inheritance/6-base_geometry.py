#!/usr/bin/python3

"""Module containing a geometry class"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Throws an `area` exception"""
        raise Exception("area() is not implemented")
