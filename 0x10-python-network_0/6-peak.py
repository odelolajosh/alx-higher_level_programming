#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    """ Finds a peak inside a list """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)
    arr = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return arr[mid]

    if mid - 1 < 0:
        return arr[mid] if arr[mid] > arr[mid + 1] else arr[mid + 1]

    if mid + 1 >= length:
        return arr[mid] if arr[mid] > arr[mid - 1] else arr[mid - 1]

    if arr[mid - 1] < arr[mid] > arr[mid + 1]:
        return arr[mid]

    if arr[mid + 1] > arr[mid - 1]:
        return find_peak(arr[mid:])

    return find_peak(arr[:mid])
