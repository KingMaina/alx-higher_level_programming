#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest_value = None
    for value in a_dictionary.values():
        if biggest_value is None or value > biggest_value:
            bigest_value = value
    return biggest_value
