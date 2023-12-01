#!/usr/bin/python3

"""Script that sends a request to a URL argument and displays the
    body of the reponse

    Usage: ./3-error_code.py <URL>
        - Displays the response body
"""

if __name__ == '__main__':
    from sys import argv
    import urllib.request
    from urllib.error import HTTPError

    URL = argv[1]
    request = urllib.request.Request(URL)
    try:
        response = urllib.request.urlopen(request)
    except HTTPError as error:
        print('Error code: {}'.format(error.code))
    else:
        print(response.read().decode('utf-8'))
