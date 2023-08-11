#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def calculate(num1, num2, operator):
    return int(num1) operator int(num2)

def main():
    operators = ["+", "-", "*", "/"]
    args = sys.argv.copy()[1:]
    args_len = len(args)
    operator = args[1]
    num1 = args[0]
    num2 = args[2]
    if args_len != 3:
        print(f"Usage: {sys.args[0]} <a> <operator> <b>")
        sys.exit(1)
    if operator not in operators:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    match operator:
        case "+":
            result = calculate(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    main()
