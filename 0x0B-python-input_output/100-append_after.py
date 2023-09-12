#!/usr/bin/python3

"""Module for file operations"""


def append_after(filename="", searchstring="", new_string=""):
    """Appends a new string after a searched string is found"""
    with open(filename, mode="w+", encoding="utf-8") as file:
        new_file = ""
        for line in file:
            print(line)
            new_file += line
            if searchstring in line:
                new_file += new_string
        file.write(new_file)
