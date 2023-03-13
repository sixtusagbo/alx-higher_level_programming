#!/usr/bin/python3
"""
Sends a POST request to a URL with email as parameter
    Args:
        url: The URL to be requested
        email: The email address to be used as parameter
"""
from sys import argv
import requests

if __name__ == '__main__':
    response = requests.post(argv[1], data={'email': argv[2]})
    print('{}'.format(response.text))
