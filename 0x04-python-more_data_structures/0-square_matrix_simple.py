#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix

    Args:
        matrix: is a 2 dimensional array

    Return:
        A new matrix of same size. Each value should be
        the square of the value of the input
    """
    return [[elem ** 2 for elem in row] for row in matrix]
