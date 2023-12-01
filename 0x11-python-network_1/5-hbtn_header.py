#!/usr/bin/python3

"""Script that takes a URL argument and displays the value of
    the response header 'X-Request-Id'
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    URL = argv[1]
    response = requests.get(URL)
    print(response.headers.get('X-Request-Id'))
