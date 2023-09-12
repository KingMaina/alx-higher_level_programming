#!/usr/bin/python3

"""Module for file appending operations"""


def append_write(filename="", text=""):
    """Appends `text` to the file

        Args:
            filename (str): Path to the file
            text (str): String to append to a file

        Returns:
            Number of bytes appended to a file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
