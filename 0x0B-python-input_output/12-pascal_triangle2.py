#!/usr/bin/python3
"""
12-pascal_triangle Module
    Contains a function that returns a list of list of integers representing
    the Pascal's triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of n

    Args:
        n (int): order of the triangle

    Return:
        (list): list representation of pascal triangle
    """
    triangle = []

    if n <= 0:
        return []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        
         

    return triangle
