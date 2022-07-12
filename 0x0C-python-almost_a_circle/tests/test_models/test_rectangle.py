#!/usr/bin/python3
""" Module for Testing Base class """
from io import StringIO
import sys
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test suite for Base class"""

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_instantiate_with_all_args(self):
        """ Test creation of `Rectangle object` """
        r = Rectangle(10, 11, 1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 11)

    def test_instantiate_with_two_args(self):
        """Test creation of `Rectangle object` with two arguments
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_min_number_of_args(self):
        """ A `Rectangle` can't be instantiated with less than 2 args """
        with self.assertRaises(TypeError):
            new = Rectangle(1)

        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_max_number_of_args(self):
        """ A `Rectangle` can't be instantiated with more than 5 args """
        with self.assertRaises(TypeError):
            new = Rectangle(1, 1, 1, 1, 1, 1)

    def test_inheritance(self):
        """ A `Rectangle` object must be an instance of the `Base` class """
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)

    def test_access_private_attrs1(self):
        """ Trying to access to a private attribute """
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__width

    def test_access_private_attrs2(self):
        """ Trying to access to a private attribute """
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__height

    def test_access_private_attrs3(self):
        """ Trying to access to a private attribute """
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__x

    def test_access_private_attrs4(self):
        """ Trying to access to a private attribute """
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__y

    def test_negative_width_and_height(self):
        """ `width` and `height` must be greater than 0 """
        with self.assertRaises(ValueError):
            r = Rectangle(-10, -1)

        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.width = -10

        with self.assertRaises(ValueError):
            r.height = -1

    def test_zero_width_and_height(self):
        """ `width` and `height` must be greater than 0 """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0)

        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.width = 0

        with self.assertRaises(ValueError):
            r.height = 0

    def test_non_int_width_and_height1(self):
        """ `width` and `height` must be an int """
        with self.assertRaises(TypeError):
            r = Rectangle("1", "Hey")

        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.width = "Width"

        with self.assertRaises(TypeError):
            r.height = "Height"

    def test_non_int_width_and_height2(self):
        """ `width` and `height` must be an int """
        with self.assertRaises(TypeError):
            r = Rectangle(1,  {})

        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.height = (0,)

        with self.assertRaises(TypeError):
            r.height = []

    def test_area1(self):
        """ test `area()` """
        r = Rectangle(1, 1)
        self.assertEqual(r.area(), 1)

    def test_area2(self):
        """ test `area()` """
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

        r.width = 4
        self.assertEqual(r.area(), 12)

        r.height = 5
        self.assertEqual(r.area(), 20)

    def test_area3(self):
        """ x, y values does not alter the area """
        r1 = Rectangle(2, 3, 13, 0)
        r2 = Rectangle(2, 3, 12, 12)

        self.assertEqual(r1.area(), r2.area())

    @patch("sys.stdout", new=StringIO())
    def test_display1(self):
        """ `display()` should show a CLI display is the Rectangle """
        r = Rectangle(2, 2)
        r.display()

        res = "##\n##\n"
        self.assertEqual(sys.stdout.getvalue(), res)
        sys.stdout.close()

    def test_display2(self):
        """ `display()` should show a CLI display is the Rectangle """
        r = Rectangle(4, 3)
        res = "####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as stdout:
            r.display()
            self.assertEqual(stdout.getvalue(), res)

        r.width = 2
        res = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as stdout:
            r.display()
            self.assertEqual(stdout.getvalue(), res)

    def test_display3(self):
        """ `display()` should show x, y offsets """
        r = Rectangle(4, 3, 1, 2)
        res = "\n\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as stdout:
            r.display()
            self.assertEqual(stdout.getvalue(), res)

    def test_display4(self):
        """ `id` values does not alter the display  """
        r1 = Rectangle(4, 3, 1, 2, 3)
        r2 = Rectangle(4, 3, 1, 2, 7)

        with patch('sys.stdout', new=StringIO()) as stdout:
            r1.display()
            v1 = stdout.getvalue()

        with patch('sys.stdout', new=StringIO()) as stdout:
            r2.display()
            v2 = stdout.getvalue()

        self.assertEqual(v1, v2)

    @patch("sys.stdout", new=StringIO())
    def test_print1(self):
        """ Should print `Rectangle` in valid format """
        r = Rectangle(4, 3)
        res = "[Rectangle] (1) 0/0 - 4/3\n"
        print(r)
        self.assertEqual(sys.stdout.getvalue(), res)

    @patch("sys.stdout", new=StringIO())
    def test_print2(self):
        """ Should print `Rectangle` in valid format """
        r = Rectangle(4, 3, 13, 45, 67)
        res = "[Rectangle] (67) 13/45 - 4/3\n"
        print(r)
        self.assertEqual(sys.stdout.getvalue(), res)

    @patch("sys.stdout", new=StringIO())
    def test_print3(self):
        """ The string value of two 'equal' `Rectangle` should be equal """
        r1 = Rectangle(4, 3, 13, 45, 67)
        r2 = Rectangle(4, 3, 13, 45, 67)
        self.assertEqual(str(r1), str(r2))

    def test_to_dictionary1(self):
        """ Resulting dictionary must contain id, size, x, y """
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()

        self.assertTrue(type(r_dict) is dict)
        self.assertIn("id", r_dict)
        self.assertIn("x", r_dict)
        self.assertIn("y", r_dict)
        self.assertIn("width", r_dict)
        self.assertIn("height", r_dict)

    def test_to_dictionary2(self):
        """ Resulting dictionary must be valid """
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r_res = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}

        self.assertTrue(type(r_dict) is dict)
        self.assertDictEqual(r_dict, r_res, "Dictionary are not equal")

    def test_to_update1(self):
        """ `update()` should update all appropriate fields """
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r_res = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}

        self.assertDictEqual(r_dict, r_res, "Dictionary are not equal")

        r.update(6, 5, 4, 3, 2)
        r_dict = r.to_dictionary()
        r_res = {"width": 5, "height": 4, "x": 3, "y": 2, "id": 6}

        self.assertDictEqual(r_dict, r_res, "Dictionary are not equal")

    def test_to_update2(self):
        """ `update()` should accept non-keyworded args """
        r = Rectangle(1, 2, 3, 4, 5)

        new_args = 6, 5, 4, 3, 2
        r.update(*new_args)
        r_dict = r.to_dictionary()
        r_res = {"width": 5, "height": 4, "x": 3, "y": 2, "id": 6}

        self.assertDictEqual(r_dict, r_res, "Dictionary are not equal")

    def test_to_update3(self):
        """ Resulting dictionary must be valid """
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r_res = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}

        self.assertDictEqual(r_dict, r_res, "Dictionary are not equal")

        r.update(27)
        r_dict = r.to_dictionary()
        r_res = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 27}

        self.assertDictEqual(r_dict, r_res, "Dictionary are not equal")

        r.update("Hey")
        r_dict = r.to_dictionary()
        r_res = {"width": 1, "height": 2, "x": 3, "y": 4, "id": "Hey"}

        self.assertDictEqual(r_dict, r_res, "Dictionary are not equal")

    def test_to_update4(self):
        """ field validation are still involved in `update()` """
        r = Rectangle(1, 2, 3, 4, 5)

        with self.assertRaises(ValueError):
            r.update("Hey", 0)

        with self.assertRaises(ValueError):
            r.update("Hey", 17, -23)

        with self.assertRaises(TypeError):
            r.update("Hey", 17, 23, "x")

        with self.assertRaises(ValueError):
            r.update("Hey", 17, 23, -4, "y")

        with self.assertRaises(TypeError):
            r.update("Hey", 17, 23, 4, "y")

        with self.assertRaises(TypeError):
            r.update("Hey", 17, 23, 4, {})

    def test_to_update5(self):
        """ `update()` should keyworded args """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 5, 6, 7, 8)

        r2.update(**r1.to_dictionary())
        self.assertDictEqual(
            r1.to_dictionary(),
            r2.to_dictionary(),
            "Dictionary are not equal"
        )

    def test_to_update6(self):
        """ `update()` should prioritize non-keyword args over
        keyworded args """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 5, 6, 7, 8)
        new_args = 6, 5, 4, 3, 2

        r2.update(*new_args, **r1.to_dictionary())
        self.assertNotEqual(r1.to_dictionary(), r2.to_dictionary())
        r2_res = {"width": 5, "height": 4, "x": 3, "y": 2, "id": 6}
        self.assertEqual(r2.to_dictionary(), r2_res)

    def test_create1(self):
        """ test `create()` """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))

    def test_create2(self):
        """ test `create()` """
        r_dict = {"width": 5, "height": 4, "x": 3, "y": 2, "id": 6}
        r: Rectangle = Rectangle.create(**r_dict)
        self.assertEqual(r_dict, r.to_dictionary())

    def test_create3(self):
        """ test validation `create()` """
        r_dict = {"width": 0, "height": 4, "x": 3, "y": 2, "id": 6}
        with self.assertRaises(ValueError):
            r = Rectangle.create(**r_dict)

    def test_create4(self):
        """ test validation `create()` """
        r_dict = {"width": 10, "height": 4, "x": -1, "y": 2, "id": "Hey"}
        with self.assertRaises(ValueError):
            r = Rectangle.create(**r_dict)

    def test_create5(self):
        """ test validation `create()` """
        r_dict = {"width": "width", "height": 4, "x": 1, "y": 2, "id": "Hey"}
        with self.assertRaises(TypeError):
            r = Rectangle.create(**r_dict)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        r1_s = [r1, r2]
        Rectangle.save_to_file(r1_s)
        r2_s = Rectangle.load_from_file()

        for r1_, r2_ in zip(r1_s, r2_s):
            self.assertEqual(str(r1_), str(r2_))


if __name__ == '__main__':
    unittest.main()
