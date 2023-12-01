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
    letter = "" if len(argv) == 1 else argv[1]
    response = requests.post(URL, data={"q": letter})
    try:
        result = response.json()
        if result == {}:
            print('No result')
        else:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
    except ValueError:
        print('Not a valid JSON')
