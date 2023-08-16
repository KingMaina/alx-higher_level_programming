#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    value = a_dictionary.get(key, None)
    if value is None:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
