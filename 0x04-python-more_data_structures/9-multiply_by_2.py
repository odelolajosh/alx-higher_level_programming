#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Multiplies all values in a dictinary by 2
    Assuming all values are only integers

    Args:
        a_dictionary: Given dictionary

    Return:
        A new dictionary
    """
    new_list = [(k, v * 2) for k, v in a_dictionary.items()]
    # new_list becomes something like [(k1, v1), (k2, v2) ...]
    # dict() converts new_list to a dictionary
    return dict(new_list)
