#!/usr/bin/python3

"""Module containing a custom list class

    The list class only allows integers in the list
"""


class MyList(list):
    """A custom list class"""

    def __init__(self):
        """Initialize the custom list class"""
        super().__init__(self)

    def print_sorted(self):
        """Prints the sorted list in ascending order"""
        self.sort()
        print(self)
