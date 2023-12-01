#!/usr/bin/python3

"""Script that accesses the `rails` repository with the `rails` user
    and displays the `sha` and `author name` of the 10 most recent commits
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    REPO = argv[1]
    OWNER = argv[2]
    URL = 'https://api.github.com/repos/{}/{}/commits'.format(REPO, OWNER)
    headers = {
        'accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    commits = requests.get(URL, headers=headers).json()
    try:
        for commit in range(10):
            print('{}: {}'.format(
                            commits[commit].get('sha'),
                            commits[commit].get('commit').get('author').get('name')
                )
            )
    except IndexError:
        pass
