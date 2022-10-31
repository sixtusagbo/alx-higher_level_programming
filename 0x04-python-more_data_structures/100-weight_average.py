#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_products = 0
    total_items = 0

    for tup in my_list:
        sum_products += tup[0] * tup[1]
        total_items += tup[1]

    return sum_products / total_items
