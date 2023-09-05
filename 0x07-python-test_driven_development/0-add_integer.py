#!/usr/bin/python3

"""0-add_integer module

    Contains `add-integer` fuction that adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers

        Args:
            a (int or float): An integer or float
            b (int or float, optional): An integer or float

        Returns:
            int or float: The sum of `a` and `b`.

        Raises:
            TypeError: a must be an integer
            TypeError: b must be an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a == float("inf") or a == float("-inf"):
        raise ValueError("a cannot be infinifty")
    if b == float("inf") or b == float("-inf"):
        raise ValueError("b cannot be infinity")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
