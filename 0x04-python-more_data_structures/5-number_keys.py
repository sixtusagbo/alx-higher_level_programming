#!/usr/bin/python3

def number_keys(a_dictionary):
    total = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        total += 1

    return (total)
