#!/usr/bin/python3

import sys

""" Module of chess queen problem
"""

def nqueens(n):
    """Program that solves the N queens problem

    Args:
        n (int): size of the board
    """
    try:
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        if not sys.argv[1].isdigit():
            print("N must be a number")
            sys.exit(1)
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        board = [[0 for i in range(n)] for j in range(n)]
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    nqueens(sys.argv)