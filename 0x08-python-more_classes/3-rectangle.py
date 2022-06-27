#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Rectangle class:
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle Object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.height = height
        self.width = width

    def __str__(self):
        """Return string representation of the rectangle
        """
        string = ""
        if self.height == 0 or self.width == 0:
            return ""

        for i in range(self.height):
            string += ("#" * self.width) + "\n"
        return string[:-1]

    @property
    def width(self):
        """Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area
        """
        return self.height * self.width

    def perimeter(self):
        """Returns the rectangle perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
