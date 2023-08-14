#!/usr/bin/python3

def max_integer(my_list=[]):
    my_list_len = len(my_list)
    if my_list_len <= 0:
        return None
    max_number = my_list[0]
    for integer in my_list:
        if integer > max_number:
            max_number = integer
    return max_number
