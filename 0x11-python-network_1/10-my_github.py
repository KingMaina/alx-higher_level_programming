#!/usr/bin/python3

"""Script that takes ones GitHub credentials as arguments and
    uses the GitHub API to display their id
"""

if __name__ == '__main__':
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    USERNAME = argv[1]
    PASSWORD = argv[2]
    URL = 'https://api.github.com/user'
    auth = HTTPBasicAuth(USERNAME, PASSWORD)
    response = requests.get(URL, auth=auth)
    print(response.json().get('id'))
