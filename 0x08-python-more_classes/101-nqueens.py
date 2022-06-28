#!/usr/bin/python3
"""Solves N Queen Problem
"""


def isSafe(queens, row, column):
    """Checks if the queen can be placed in a position

    Args:
        queens (list): Chess board with queens positions
        row (int): row position
        column (int): column position

    Returns:
        True: if the queen can be placed at (row, column)
        False: If the queen can't be placed at (row, column)
    """
    for i in range(1, row + 1):
        # Check Column
        if queens[row - i] == column:
            return False

        # Check upleft diagonal
        if queens[row - i] == column - i:
            return False

        # Check upright diagonal
        if queens[row - i] == column + i:
            return False
    return True


def printNQueen(queens):
    """Prints positions of queens on the board

    Args:
        queens (list): List of list of position of the queens
    """
    print([[i, x] for i, x in enumerate(queens)])


def solveQueen(queens, row):
    """Returns a single solution for N Queen given a start index
    for the first queen

    Args:
        queens (list): List of list of position of the queens
        row (int): initial column value for queen at row 0

    Return:
        (list): a solution
    """
    N = len(queens)

    if row is N:
        printNQueen(queens)
        return

    queens[row] = -1

    while queens[row] < N - 1:
        queens[row] += 1
        # Check possible locations for the row
        if isSafe(queens, row, queens[row]) is True:
            if row is not N:
                solveQueen(queens, row + 1)


def nQueens(N):
    """Print every possible solution to the given N problem

    Args:
        N (int): size of chessboard
    """
    queens = [-1 for i in range(N)]
    solveQueen(queens, 0)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nQueens(N)
