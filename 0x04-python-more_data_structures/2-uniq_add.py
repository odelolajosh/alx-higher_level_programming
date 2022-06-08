#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list

    Args:
        my_list: given list

    Return:
        the sum of unique list
    """
    uniq = set(my_list)
    sum = 0;
    for m in uniq:
        sum += m;
    return sum
