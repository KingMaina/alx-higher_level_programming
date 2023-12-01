#!/usr/bin/python3

"""Script that takes a letter as an argument, sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter
    and displays the body if it is valid JSON, othrewise it displays
    an invalid message
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    URL = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] if len(argv) > 1 else ''
    response = requests.post(URL, data={'q': letter})
    try:
        result = response.json()
        if not result:
            print('No result')
        else:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
    except JSONDecodeError as error:
        print('Not a valid JSON')
