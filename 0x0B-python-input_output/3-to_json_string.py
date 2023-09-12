#!/usr/bin/python3

"""Module for json operations on files"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object

        Args:
            my_obj (object): Object

        Returns:
            The JSON representation of `my_obj`
    """
    return json.dumps(my_obj)
