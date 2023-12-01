#!/usr/bin/python3
"""
Script that takes in a URL, sends a request and displays the value
of the X-Request-Id in the response header
"""

if __name__ == '__main__':
    from sys import argv
    import urllib.request

    url = argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = response.headers
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
