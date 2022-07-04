#!/usr/bin/python3
"""
Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class from BaseGeometry class
    """

    def __init__(self, width, height):
        """ Instantiates Rectangle with width and height """
        self.integer_validator("width", width)
        self.integer_validator("heiaght", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculates area """
        return self.__width * self.__height

    def __str__(self):
        """ Returns printable string """
        cls = self.__class__.__name__
        return "[{}] {}/{}".format(cls, self.__width, self.__height)
