#!/usr/bin/python3
"""
Uses the GitHub API to display your id
    Args:
        username: Github username
        password: Github token
"""
from sys import argv
import requests


if __name__ == '__main__':
    try:
        repo = argv[1]
        owner = argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        response = requests.get(url)
        commits = response.json()
        for i in range(0, 10):
            print('{}: {}'.format(commits[i]['sha'],
                                  commits[i]['commit']['author']['name']))
    except Exception:
        pass
