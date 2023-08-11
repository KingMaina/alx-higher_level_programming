#!/usr/bin/python3
import sys


def main():
    args_len = len(sys.argv) - 1
    if args_len == 0:
        print(f"{args_len} arguments.")
        return
    elif args_len == 1:
        print(f"{args_len} argument:")
    else:
        print(f"{args_len} arguments:")
    for index in range(1, args_len + 1):
        print(f"{index}: {sys.argv[index]}")


if __name__ == "__main__":
    main()
