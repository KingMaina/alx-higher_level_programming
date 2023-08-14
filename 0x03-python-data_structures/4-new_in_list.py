#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_list_len = len(my_list)
    my_list_copy = my_list.copy()
    if my_list_len <= 0 or idx >= my_list_len:
        return my_list_copy
    my_list_copy[idx] = element
    return my_list_copy
