#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print an integer
    Args:
        value: value to print
    Return:
        True if value has been correctly printed
        False if otherwise
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False

    return True
