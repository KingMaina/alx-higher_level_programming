#!/usr/bin/python3

"""Module for writing an object into a JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using
        a JSON representation

        Args:
            my_obj (object): Object
            filename (str): Path to the file

        Returns:
            None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        my_obj_json = json.dumps(my_obj)
        return file.write(my_obj_json)
