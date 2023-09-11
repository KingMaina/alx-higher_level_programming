#!/usr/bin/python3

"""101-add_attribute module

    Contains a function that adds a new attribute
    to an object if possible
"""


def add_attribute(obj, key, value):
    """Adds an attribute to an object

        Args:
            obj (object) - An object
            key (str) - The attribute name to add
            value (object) - The value to assign to the key
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
