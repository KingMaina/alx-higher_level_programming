#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dict_keys = sorted(a_dictionary.keys())
    for key in sorted_dict_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
