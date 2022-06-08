#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple (<score>, <weight>).

    Args:
        my_list: Given list

    Return:
        The weighted average
    """
    total_score, total_weight = 0, 0

    if len(my_list) == 0:
        return 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight
