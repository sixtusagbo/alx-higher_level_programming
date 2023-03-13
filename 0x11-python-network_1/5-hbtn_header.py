#!/usr/bin/python3
"""
Request URL and displays the value of the variable X-Request-Id
in response header
    Args:
        url: url address to request
"""
import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    print(response.headers['X-Request-Id'])
