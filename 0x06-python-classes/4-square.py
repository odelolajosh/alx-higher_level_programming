#!/usr/bin/python3
"""
Square Class Module
"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0):
        """Initialize the square object
        """
        self.size = size

    @property
    def size(self):
        """Getter for the size attribute of the square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute of the square object
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the current square area
        """
        return self.__size ** 2
