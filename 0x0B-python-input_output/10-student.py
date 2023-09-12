#!/usr/bin/python3

"""Student module"""


class Student:
    """A Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Returns the dictionary representation of a student instance"""
        if hasattr(self, "__dict__"):
            new_dict = {}
            for key, value in self.__dict__.items():
                if isinstance(value, (int, str, bool)):
                    new_dict[key] = value
                elif isinstance(value, list):
                    new_list = []
                    for item in value:
                        if isinstance(item, int, str, bool):
                            new_list.append(item)
                    new_dict[key] = new_list
                elif isinstance(value, dict):
                    inner_dict = {}
                    for key1, value2 in value.items():
                        if isinstance(value2, (int, str, bool)):
                            inner_dict[key1] = value2
                    new_dict[key] = inner_dict
            return new_dict
