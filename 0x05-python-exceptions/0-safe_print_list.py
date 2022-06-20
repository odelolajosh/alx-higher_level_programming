#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list
    Args:
        my_list: Given list
        x: count of elements to print

    Return:
        The real number of elements printed
    """
    count = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except IndexError:
            break
        else:
            count += 1

    print()
    return count
