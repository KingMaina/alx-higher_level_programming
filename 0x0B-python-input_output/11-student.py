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
        if attr is None:
            return self.__dict__
        else:
            new_dict = {}
            for attribute in attr:
                if hasattr(self, attribute):
                    new_dict[attribute] = getattr(self, attribute)
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the object instance"""
