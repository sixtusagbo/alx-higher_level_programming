#!/usr/bin/python3
"""
Sends a POST request to a URL with email as parameter
    Args:
        url: The URL to be requested
        email: The email address to be used as parameter
"""
from sys import argv
from urllib import request, parse


if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}

    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
