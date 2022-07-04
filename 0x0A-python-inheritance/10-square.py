#!/usr/bin/python3
"""
Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class from Rectangle class
    """

    def __init__(self, size):
        """Instantiates Square

        Args:
            size (int): The length of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Calculates area """
        return super().area()
