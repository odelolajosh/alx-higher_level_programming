#!/usr/bin/python3
"""
Base Geometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class from BaseGeometry class
    """

    def __init__(self, width, height):
        """Instantiate with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
