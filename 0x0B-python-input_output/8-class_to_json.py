#!/usr/bin/python3

"""Class to JSON module"""


def class_to_json(obj):
    """Converts an objects attributes into a serializable form

        Args:
            obj (object) - Object instance of a class

        Returns:
            Serializable object
    """
    if hasattr(obj, "__dict__"):
        new_dict = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, (int, str, bool)):
                new_dict[key] = value
            elif isinstance(value, list):
                new_list = []
                for item in value:
                    if isinstance(item, (int, str, bool)):
                        new_list.append(item)
                new_dict[key] = new_list
            elif isinstance(value, dict):
                inner_dict = {}
                for key1, value2 in value.items():
                    if isinstance(value2, (int, str, bool)):
                        inner_dict[key1] = value2
                new_dict[key] = inner_dict
        return new_dict
