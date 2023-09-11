#!/usr/bin/python3

"""Module that contains a function to check if
    an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """Checks if `obj` is an instance of or is an instance
        of a class inherited from `a_class`

        Args:
            obj (object): An object
            a_class (class): A class

        Returns:
            True if `obj` is an instance of `a_class`, False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
