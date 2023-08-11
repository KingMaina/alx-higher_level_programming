#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculate(num1, num2, operator):
    if operator == "+":
        return add(int(num1), int(num2))
    elif operator == "-":
        return sub(int(num1), int(num2))
    elif operator == "*":
        return mul(int(num1), int(num2))
    elif operator == "/":
        return div(int(num1), int(num2))


def main():
    operators = ["+", "-", "*", "/"]
    args = sys.argv.copy()[1:]
    args_len = len(args)
    if args_len != 3:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        sys.exit(1)
    operator = args[1]
    num1 = args[0]
    num2 = args[2]
    if operator not in operators:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    result = calculate(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    main()
