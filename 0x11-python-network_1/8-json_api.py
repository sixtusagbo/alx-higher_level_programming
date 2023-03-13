#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
    Args:
        q: letter to send
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if argv[1]:
        q = argv[1]
    response = requests.post(url, data={'q': q})
    try:
        response = response.json()
        if not response:
            print('No result')
        else:
            print('[{}] {}'.format(response['id'], response['name']))
    except ValueError:
        print('Not a valid JSON')
