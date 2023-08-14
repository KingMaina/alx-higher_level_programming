#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisibles = []
    for number in my_list:
        divisibles.append(True if number % 2 == 0 else False)
    return divisibles
