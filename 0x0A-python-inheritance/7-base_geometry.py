#!/usr/bin/python3
"""
Base Geometry class
"""


class BaseGeometry:
    """An empty Geometry class
    """
    def area(self):
        """Base implementation for area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
