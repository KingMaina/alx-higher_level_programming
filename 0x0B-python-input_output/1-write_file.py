#!/usr/bin/python3

"""Module for file manipulation"""


def write_file(filename="", text=""):
    """Writes `text` into the file name

        Args:
            filename (str): Path to the file
            text (str): string to write to a file

        Returns:
            The number of bytes written into the file, 0 otherwise
    """
    number_of_bytes = 0
    with open(filename, mode="w", encoding="utf-8") as file:
        number_of_bytes = file.write(text)
    return number_of_bytes
