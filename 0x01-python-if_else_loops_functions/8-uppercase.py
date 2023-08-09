#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        print("{}".format(chr(ord(letter)) - 32), end="")
    print("".format(), end="")
