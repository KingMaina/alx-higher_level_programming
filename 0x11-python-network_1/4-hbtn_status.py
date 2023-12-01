#!/usr/bin/python3

"""Script that fetches https://alx-intranet.hbtn.io/status
    and displays the response body in a custom format
"""


if __name__ == '__main__':
    import requests

    URL = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(URL)
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))
