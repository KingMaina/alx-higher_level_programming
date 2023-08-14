#!/usr/bin/python3

def no_c(my_string):
    my_string_len = len(my_string)
    new_string = ""
    for counter in range(my_string_len):
        if my_string[counter] in "cC":
            continue
        new_string += my_string[counter]
    return new_string
