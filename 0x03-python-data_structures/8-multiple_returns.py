#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a
    string and its first character

    Args:
        sentence: Given string

    Return:
        Tuple with length and first character
    """
    length = len(sentence)

    if length == 0:
        return (length, None)

    return (length, sentence[0])
