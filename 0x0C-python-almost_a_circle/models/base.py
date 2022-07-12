#!/usr/bin/python3
""" Base class """
import csv
import json
import os
import random
import time
import turtle


class Base:
    """Base class
        auto increments id for each instance with `None` id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base class

        Args:
            id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a json file
            Args:
                list_objs (list): list of `Base` instances
        """
        filename = "{}.json".format(cls.__name__)
        json_list = []

        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())

        with open(filename, "w") as f:
            json.dump(json_list, f)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates a new `Base` instance from a dictionary of attributes """
        params = [10, 10]
        obj = cls(*params)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ Load a list of `Base` instance from json file """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as f:
            json_content = f.read()

        parsed = cls.from_json_string(json_content)

        obj_list = []
        for param in parsed:
            obj_list.append(cls.create(**param))

        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save object in a file """
        filename = "{}.csv".format(cls.__name__)
        csv_format = cls.csv_format()

        rows = []
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            row = [obj_dict[item] for item in csv_format]
            rows.append(row)

        with open(filename, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """ Load a list of `Base` instance from csv file """
        filename = "{}.csv".format(cls.__name__)
        csv_format = cls.csv_format()

        if os.path.exists(filename) is False:
            return []

        obj_list = []
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                obj_dict = {}
                for key, value in zip(csv_format, row):
                    obj_dict[key] = int(value)

                obj_list.append(cls.create(**obj_dict))

        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw rectangles and squares from a list """
        unit = 2
        colors = ["white", "blue", "purple", "grey", "magenta"]

        tr = turtle.Turtle()
        tr.shape("turtle")
        tr.screen.bgcolor("black")
        tr.speed(3)

        for obj in list_rectangles + list_squares:
            tr.clear()
            tr.showturtle()
            tr.penup()
            tr.goto(obj.x * unit, obj.y * unit)
            tr.pendown()
            tr.begin_fill()
            tr.color(random.choice(colors))
            tr.forward(obj.width * unit)
            tr.left(90)
            tr.forward(obj.height * unit)
            tr.left(90)
            tr.forward(obj.width * unit)
            tr.left(90)
            tr.forward(obj.height * unit)
            tr.left(90)
            tr.end_fill()
            tr.penup()
            tr.hideturtle()
            time.sleep(1)

        time.sleep(3)
        turtle.bye()
