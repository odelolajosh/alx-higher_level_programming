#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list

    Args:
        my_list: given list

    Return:
        max integer if list is not empty else None
    """
    if not my_list:
        return None

    max = my_list[0]
    for n in my_list:
        if max < n:
            max = n
    return max
