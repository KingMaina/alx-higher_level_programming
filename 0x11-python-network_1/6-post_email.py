#!/usr/bin/python3

"""Script that takes in a URL and email address, sends as POST
    request with the email and displays the body of the response
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    URL = argv[1]
    EMAIL = argv[2]
    response = requests.post(URL, data={'email': EMAIL})
    print(response.text)
