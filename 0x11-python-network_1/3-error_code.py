#!/usr/bin/python3
"""
Displays bofy od response and error code if any
    Args:
        url: The URL to be requested
"""
from sys import argv
from urllib import request, parse, error


if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
