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
    url = 'https://api.github.com/user'
    username = argv[1]
    token = argv[2]
    headers = {'Authorization': 'token {}'.format(token)}
    response = requests.get(url, headers=headers)
    print(response.json().get('id'))
