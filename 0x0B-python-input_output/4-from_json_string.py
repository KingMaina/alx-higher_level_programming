#!/usr/bin/python3

"""Module for converting JSON to python object"""
import json


def from_json_string(my_str):
    """Converts JSON to python object

        Args:
            my_str (str): JSON string

        Returns:
            Object rep. of a JSON string
    """
    return json.loads(my_str)
