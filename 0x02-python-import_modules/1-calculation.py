#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    a = 10
    b = 5
    a = add(10, 5)
    print(f"10 + 5 = {a}")
    a = sub(10, 5)
    print(f"10 - 5 = {a}")
    a = mul(10, 5)
    print(f"10 * 5 = {a}")
    a = div(10, 5)
    print(f"10 / 5 = {a}")
