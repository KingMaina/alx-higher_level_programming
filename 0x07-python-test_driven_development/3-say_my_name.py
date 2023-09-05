#!/usr/bin/python3

""" Print name module

    Functions:
        say_my_name(first_name, last_name=""):
            Prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """Prints the first and last name

        Args:
            first_name (str): The first name
            last_name (str): The last name

        Returns:
            None

        Raises:
            TypeError: first_name must be a string
            TypeError: last_name must be a string
            TypeError: say_my_name() missing 1 required positional
                argument: 'first_name'
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
