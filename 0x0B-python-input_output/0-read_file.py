#!/usr/bin/python3

"""Module containing functions operating on files"""


def read_file(filename=""):
    """Reads the contents of a text file

        Args:
            filename (str): Path to the file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
        print()
