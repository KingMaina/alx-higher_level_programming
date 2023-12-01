#!/usr/bin/python3

"""
A script that fetches https://alx-intranet.hbtn.io/status
using urllib python package
"""

if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(page)))
    print('\t- content: {}'.format(page))
    print('\t- utf8 content: {}'.format(page.decode('utf-8')))
