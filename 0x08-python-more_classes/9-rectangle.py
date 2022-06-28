#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Rectangle class:
    Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle Object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """Return string representation of the rectangle
        """
        string = ""
        if self.height == 0 or self.width == 0:
            return ""

        for i in range(self.height):
            string += (str(self.print_symbol) * self.width) + "\n"
        return string[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle to be
        able to recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Prints a message when the instance is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle based on the area

        Args:
            rect_1 (Rectangle): Rectangle 1
            rect_2 (Rectangle): Rectangle 2

        Return:
            The bigger rectangle

        Raises:
            TypeError: if a rect_1 or rect_2 is not a Rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size

        Args:
            cls (Rectangle): Rectangle class
            size (int): size of the square

        Returns:
            New instance of the Rectangle representing a square
        """
        return cls(size, size)
