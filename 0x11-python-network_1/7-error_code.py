#!/usr/bin/python3

"""Script that takes a URL, sends a request to it and diplays the
    response body or error code if it is >=400
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    URL = argv[1]
    response = requests.get(URL)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
