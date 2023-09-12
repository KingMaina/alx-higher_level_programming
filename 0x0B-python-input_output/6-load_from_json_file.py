#!/usr/bin/python3

""""JSON manipulation module
    contains a function that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

        Args:
        filename (str): Name/path of the file

        Returns:
            None
    """
    with open(filename, mode="r", encoding='utf-8') as file:
        return json.load(file)
