#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_len = len(tuple_a)
    tuple_b_len = len(tuple_b)

    if tuple_a_len >= 2:
        number1 = tuple_a[0]
        number2 = tuple_a[1]
    elif tuple_a_len == 1:
        number1 = tuple_a[0]
        number2 = 0
    elif tuple_a_len <= 0:
        number1 = number2 = 0
    if tuple_b_len >= 2:
        number3 = tuple_b[0]
        number4 = tuple_b[1]
    elif tuple_b_len == 1:
        number3 = tuple_b[0]
        number4 = 0
    elif tuple_b_len <= 0:
        number3 = number4 = 0
    return (number1 + number3, number2 + number4)
