#!/usr/bin/python3

"""
Script that makes a POST request to a URL passed as an argument
and displays the decoded body response in utf-8
"""

if __name__ == '__main__':
    from sys import argv
    import urllib.request
    import urllib.parse

    URL = argv[1]
    EMAIL = argv[2]
    values = {'email': EMAIL}
    data = urllib.parse.urlencode(values).encode('ascii')
    request = urllib.request.Request(URL, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
