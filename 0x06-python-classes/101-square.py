#!/usr/bin/python3
"""
Square Class Module
"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square object
        """
        self.size = size
        self.position = position

    def __str__(self):
        """Returns string for a Square instance
        """
        string = ""

        if self.size == 0:
            return "\n"

        for i in range(self.position[1]):
            string += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                string += " "
            for k in range(self.size):
                string += "#"
            if i < self.size - 1:
                string += "\n"

        return string

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

    @property
    def position(self):
        """Getter for the property sttribute of the square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for property attribute of the square object
        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
            return

        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for k in range(self.size):
                print("#", end="")
            print()
