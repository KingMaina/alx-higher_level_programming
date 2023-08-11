#!/usr/bin/python3
import sys

def main():
    argsCopy = sys.argv.copy()[1:]
    argsLen = len(argsCopy) - 1
    total = 0
    for argument in argsCopy:
        total += int(argument)
    print(f"{total}")

if __name__ == "__main__":
    main()
