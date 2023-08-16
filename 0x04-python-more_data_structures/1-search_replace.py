#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for index, value in enumerate(my_list):
        if value == search:
            value = replace
        new_list.append(value)
    return new_list
