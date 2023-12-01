#!/usr/bin/python3

"""Script that accesses the `rails` repository with the `rails` user
    and displays the `sha` and `author name` of the 10 most recent commits
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    REPO = argv[1]
    OWNER = argv[2]
    URL = 'https://api.github.com/repos/{}/{}/commits'.format(OWNER, REPO)
    commits = requests.get(URL).json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                            commits[i].get('sha'),
                            commits[i].get('commit').get('author').get('name')
                )
            )
    except IndexError:
        pass
