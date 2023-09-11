#!/usr/bin/python3

"""Module containing a function to lookup the attributes
    and methods of an object
"""


def lookup(myObject):
    """Returns a list of attributes and methods of the object

        Args:
            object (object) - a valid python object
    """
    if (issubclass(myObject, object)):
        return dir(myObject)
