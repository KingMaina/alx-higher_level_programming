#!/usr/bin/python3

"""Module that contains a function to check if
    an object inherits from a given class
"""


def inherits_from(obj, a_class):
    """Checks if an `obj` is is an instance
    of a class that inherited (directly or indirectly)
    from the specified class

        Args:
            obj (object): An object
            a_class (class): A class

        Returns:
            True if `obj` is inherited from `a_class`, False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
