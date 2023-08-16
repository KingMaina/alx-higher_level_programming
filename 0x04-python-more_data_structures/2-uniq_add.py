#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_list = set(my_list.copy())
    sum = 0
    for value in unique_list:
        sum += value
    return sum
