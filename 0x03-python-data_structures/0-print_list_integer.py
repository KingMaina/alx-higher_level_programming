#!/usr/bin/python3

def print_list_integer(my_list=[]):
    my_list_len = len(my_list)
    if my_list_len > 0:
        for item in my_list:
            print("{}".format(item))
