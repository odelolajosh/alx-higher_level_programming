#!/usr/bin/python3
""" Module for Testing Base class """
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test suite for Base class"""

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test implicitly assigned id """
        b1 = Base(1)
        self.assertAlmostEqual(b1.id, 1)

    def test_auto_id(self):
        """ Test auto assigned id """
        b2 = Base()
        self.assertAlmostEqual(b2.id, 1)

    def test_id_inc(self):
        """ Test __nb_objects increment """
        b1 = Base(1)
        b2 = Base()
        b3 = Base()
        self.assertAlmostEqual(b3.id, 2)
        b4 = Base(12)
        self.assertAlmostEqual(b4.id, 12)
        b5 = Base()
        self.assertAlmostEqual(b5.id, 3)

    def test_str_id(self):
        """ Test string id """
        b = Base("id")
        self.assertEqual(b.id, "id")

    def test_with_two_args(self):
        """ Test passing n-args to init method """
        with self.assertRaises(TypeError):
            b = Base(1, 1)
    
    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """
        b = Base(1)
        with self.assertRaises(AttributeError):
            b.__nb_objects

    def test_save_json_to_file_rect(self):
        """ Test saving Rectangle as json """
        Rectangle.save_to_file(None)
        filename = "{}.json".format(Rectangle.__name__)
        expected = "[]"

        with open(filename, "r") as f:
            actual = f.read()
            self.assertEqual(actual, expected)

        Rectangle.save_to_file([
            Rectangle(10, 7, 2, 8),
            Rectangle(1, 1)
        ])
        r1 = '{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}'
        r2 = '{"id": 2, "width": 1, "height": 1, "x": 0, "y": 0}'
        expected = "[{}, {}]".format(r1, r2)

        with open(filename, "r") as f:
            actual = f.read()
            self.assertEqual(actual, expected)

        try:
            os.remove(filename)
        except Exception:
            pass

    def test_save_json_to_file_square(self):
        """ Test saving Square as json """
        Square.save_to_file(None)
        filename = "{}.json".format(Square.__name__)
        expected = "[]"

        with open(filename, "r") as f:
            actual = f.read()
            self.assertEqual(actual, expected)

        Square.save_to_file([
            Square(10, 2, 8),
            Square(1)
        ])
        r1 = '{"id": 1, "size": 10, "x": 2, "y": 8}'
        r2 = '{"id": 2, "size": 1, "x": 0, "y": 0}'
        expected = "[{}, {}]".format(r1, r2)

        with open(filename, "r") as f:
            actual = f.read()
            self.assertEqual(actual, expected)

        try:
            os.remove(filename)
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
