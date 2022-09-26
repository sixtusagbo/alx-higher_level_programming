#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position
    without modifying the original list.

    Args:
        my_list: list to work with
        idx: index
        element: new element

    Returns:
        A new list with the element replaced at idx
    """
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element

    return new_list
