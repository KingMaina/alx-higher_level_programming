#!/usr/bin/python3

"""Module containing a script that works on JSON files"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file'
    ).load_from_json_file


if __name__ == "__main__":
    def main():
        """Saves the arguments to the program in a JSON file"""
        args = sys.argv[1:]
        save_to_json_file(args, "add_item.json")
        return load_from_json_file("add_item.json")
    main()
