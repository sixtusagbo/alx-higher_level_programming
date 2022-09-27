#!/usr/bin/python3

def max_integer(my_list=[]):
    """ finds the biggest integer of in a list

    Args:
        max_num: the result

    Returns:
        max_num
    """
    if not my_list:
        return None

    max_num = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > max_num:
            max_num = my_list[i]

    return max_num
