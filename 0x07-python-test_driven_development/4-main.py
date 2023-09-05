#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    # print_square(-1)
    # print_square(None)
    # print_square([1, 2, -5])
    # print_square({"one": 1, "two": 2})
    # print_square((4, -10))
    # print_square(5, None)
    # print_square()
    print_square(1e999)
except Exception as e:
    print(e)
print("")
