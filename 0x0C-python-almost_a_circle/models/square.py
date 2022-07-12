#!/usr/bin/python3
""" Module for Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return string representation of the rectangle """
        str_name = "[{}]".format(self.__class__.__name__)
        str_id = "({:d})".format(self.id)
        str_pos = "{:d}/{:d}".format(self.x, self.y)
        str_dim = "{:d}".format(self.size)
        return str_name + " " + str_id + " " + str_pos + " - " + str_dim

    def update(self, *args, **kwargs):
        """ Update the class """
        if args is not None and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for attr, arg in zip(attrs, args):
                if attr == "size":
                    setattr(self, "width", arg)
                    setattr(self, "height", arg)
                else:
                    setattr(self, attr, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return dictionary representation of the object """
        __dict = {}
        attrs = ["id", "size", "x", "y"]
        for attr in attrs:
            if attr == "size":
                __dict[attr] = getattr(self, "width")
            else:
                __dict[attr] = getattr(self, attr)
        return __dict

    @staticmethod
    def csv_format():
        """ Return the csv row format for `Square` class """
        return ["id", "size", "x", "y"]
