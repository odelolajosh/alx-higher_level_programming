#!/usr/bin/python3
""" Module for Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle class

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x coordinate of the rectangle
            y: y coordinate of the rectangle
            id: id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Print the rectangle """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ Return string representation of the rectangle """
        str_name = "[{}]".format(self.__class__.__name__)
        str_id = "({:d})".format(self.id)
        str_pos = "{:d}/{:d}".format(self.x, self.y)
        str_dim = "{:d}/{:d}".format(self.width, self.height)
        return str_name + " " + str_id + " " + str_pos + " - " + str_dim

    def update(self, *args, **kwargs):
        """ Update the class """
        if args is not None and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return dictionary representation of the object """
        __dict = {}
        attrs = ["id", "width", "height", "x", "y"]
        for attr in attrs:
            __dict[attr] = getattr(self, attr)
        return __dict

    @staticmethod
    def csv_format():
        """ Return the csv row format for `Rectangle` class """
        return ["id", "width", "height", "x", "y"]
