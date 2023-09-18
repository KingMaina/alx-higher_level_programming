#!/usr/bin/python3

"""A module containing a Base class"""
import json


class Base:
    """A base class

        Attributes:
            __nb_objects (int): Number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class

            Args:
                id (int): Id of a created object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of `list_dictionaries`"""
        if list_dictionaries and list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON representation of a shape to a file

            Args:
                list_objs (list): List of object\
                    instances of the `Base` class
        """
        if list_objs is None:
            json_objs = cls.to_json_string([])
        else:
            json_list = [obj.to_dictionary() for obj in list_objs]
            json_objs = cls.to_json_string(json_list)
        with open("{}.json".format(cls.__name__),
                  mode="w", encoding="utf-8") as file:
            file.write(json_objs)

    @staticmethod
    def from_json_string(json_string):
        """Convert the JSON `json_string`

            Args:
                `json_string` (str): a JSON string representing\
                    a list of dictionaries
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a shape instance from `dictionary`"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        cls.update(new_instance, **dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file"""
        instances = []
        try:
            with open(cls.__name__ + ".json",
                      mode="r", encoding="utf-8") as file:
                list_content = cls.from_json_string(file.read())
                for obj in list_content:
                    instances.append(cls.create(**obj))
                return instances
        except FileNotFoundError:
            return instances
