#!/usr/bin/python3
'''
Fetches https://alx-intranet.hbtn.io/status
'''
from urllib import request


with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    the_page = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(the_page)))
    print('\t- content: {}'.format(the_page))
    print('\t- utf8 content: {}'.format(the_page.decode('utf-8')))
