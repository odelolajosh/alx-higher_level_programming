#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list

    Args:
        my_list: given list
        idx: index for item to be deleted

    Return:
        the modified list
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]

    return my_list
