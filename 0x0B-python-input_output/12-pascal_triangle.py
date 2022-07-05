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
            continue

        row = []
        prev = [0] + triangle[i - 1] + [0]

        # Sliding Window Algorithm
        runningSum = 0
        for i in range(len(prev)):
            runningSum += prev[i]

            if i >= 1:
                row.append(runningSum)
                runningSum -= prev[i - 1]

        triangle.append(row)
    return triangle
