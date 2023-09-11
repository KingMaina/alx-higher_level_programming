#!/usr/bin/python3

"""Module that contains a function to check if
    an object is from a given class
"""


def is_same_class(obj, a_class):
    """Checks if an `obj` is an instance of `a_class`

        Args:
            obj (object): An object
            a_class (class): A class

        Returns:
            True if `obj` is of type `a_class`, False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
