#!/usr/bin/python3
""" Module for Testing Base class """
from io import StringIO
import sys
import unittest
from unittest.mock import patch
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquareClass(unittest.TestCase):
    """Test suite for Base class"""

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_instantiate_with_all_args(self):
        """ Test creation of `Square object` """
        r = Square(10, 1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.size, 10)

    def test_instantiate_with_two_args(self):
        """Test creation of `Square object` with two arguments
        """
        r = Square(1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.size, 1)

    def test_min_number_of_args(self):
        """ A `Square` can't be instantiated with less than 1 args """
        with self.assertRaises(TypeError):
            s = Square()

    def test_max_number_of_args(self):
        """ A `Square` can't be instantiated with more than 4 args """
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1, 1, 1)

    def test_inheritance(self):
        """ A `Square` object must be an instance of the `Base` class """
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_access_private_attrs1(self):
        """ Trying to access to a private attribute """
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__width

    def test_access_private_attrs2(self):
        """ Trying to access to a private attribute """
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__height

    def test_access_private_attrs3(self):
        """ Trying to access to a private attribute """
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__x

    def test_access_private_attrs4(self):
        """ Trying to access to a private attribute """
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__y

    def test_negative_width_and_height(self):
        """ `width` and `height` must be greater than 0 """
        with self.assertRaises(ValueError):
            s = Square(-10)

        s = Square(1)
        with self.assertRaises(ValueError):
            s.size = -10

        with self.assertRaises(ValueError):
            s.width = -1
        
        with self.assertRaises(ValueError):
            s.height = -1

    def test_zero_width_and_height(self):
        """ `width` and `height` must be greater than 0 """
        with self.assertRaises(ValueError):
            s = Square(0)

        s = Square(1)
        with self.assertRaises(ValueError):
            s.size = 0

        with self.assertRaises(ValueError):
            s.width = 0

        with self.assertRaises(ValueError):
            s.height = 0

    def test_non_int_width_and_height1(self):
        """ `width` and `height` must be an int """
        with self.assertRaises(TypeError):
            s = Square("1")

        s = Square(1)
        with self.assertRaises(TypeError):
            s.size = "Size"
        
        with self.assertRaises(TypeError):
            s.width = "Width"

        with self.assertRaises(TypeError):
            s.height = "Height"

    def test_non_int_width_and_height2(self):
        """ `width` and `height` must be an int """
        with self.assertRaises(TypeError):
            r = Square(1,  {})

        r = Square(1, 1)
        with self.assertRaises(TypeError):
            r.height = (0,)

        with self.assertRaises(TypeError):
            r.height = []
    
    def test_size1(self):
        """ `width` and `height` must be equal to size """
        s = Square(21)
        self.assertEqual(s.size, s.width)
        self.assertEqual(s.size, s.height)
    
    def test_size2(self):
        """ `width` and `height` must be equal to size """
        s = Square(21)
        self.assertEqual(s.size, s.width)
        self.assertEqual(s.size, s.height)
        s.size = 5
        self.assertEqual(5, s.size)
        self.assertEqual(5, s.height)

    def test_area1(self):
        """ test `area()` """
        s = Square(21)
        self.assertEqual(s.area(), 21**2)

    def test_area2(self):
        """ test `area()` """
        s = Square(2)
        self.assertEqual(s.area(), 4)

        s.size = 4
        self.assertEqual(s.area(), 16)

        s.size = 5
        self.assertEqual(s.area(), 25)

    def test_area3(self):
        """ x, y values does not alter the area """
        s1 = Square(2, 13, 0)
        s2 = Square(2, 12, 12)

        self.assertEqual(s1.area(), s2.area())

    @patch("sys.stdout", new=StringIO())
    def test_display1(self):
        """ `display()` should show a CLI display of the Square """
        s = Square(2)
        s.display()

        res = "##\n##\n"
        self.assertEqual(sys.stdout.getvalue(), res)
        sys.stdout.close()

    def test_display2(self):
        """ `display()` should show a CLI display of the Square """
        s = Square(4)
        res = "####\n"*4
        with patch('sys.stdout', new=StringIO()) as stdout:
            s.display()
            self.assertEqual(stdout.getvalue(), res)

        s.size = 2
        res = "##\n"*2
        with patch('sys.stdout', new=StringIO()) as stdout:
            s.display()
            self.assertEqual(stdout.getvalue(), res)

    def test_display3(self):
        """ `display()` should show x, y offsets """
        s = Square(4, 1, 2)
        res = "\n\n" + " ####\n" * 4
        with patch('sys.stdout', new=StringIO()) as stdout:
            s.display()
            self.assertEqual(stdout.getvalue(), res)

    def test_display4(self):
        """ `id` values does not alter the display  """
        s1 = Square(4, 1, 2, 3)
        s2 = Square(4, 1, 2, 7)

        with patch('sys.stdout', new=StringIO()) as stdout:
            s1.display()
            v1 = stdout.getvalue()

        with patch('sys.stdout', new=StringIO()) as stdout:
            s2.display()
            v2 = stdout.getvalue()

        self.assertEqual(v1, v2)

    @patch("sys.stdout", new=StringIO())
    def test_print1(self):
        """ Should print `Square` in valid format """
        s = Square(3)
        res = "[Square] (1) 0/0 - 3\n"
        print(s)
        self.assertEqual(sys.stdout.getvalue(), res)

    @patch("sys.stdout", new=StringIO())
    def test_print2(self):
        """ Should print `Square` in valid format """
        s = Square(4, 13, 45, 67)
        res = "[Square] (67) 13/45 - 4\n"
        print(s)
        self.assertEqual(sys.stdout.getvalue(), res)

    @patch("sys.stdout", new=StringIO())
    def test_print3(self):
        """ The string value of two 'equal' `Square` should be equal """
        s1 = Square(43, 13, 45, 67)
        s2 = Square(43, 13, 45, 67)
        self.assertEqual(str(s1), str(s2))

    def test_to_dictionary1(self):
        """ Resulting dictionary must contain id, size, x, y """
        s = Square(2, 3, 4, 5)
        s_dict = s.to_dictionary()

        self.assertTrue(type(s_dict) is dict)
        self.assertIn("id", s_dict)
        self.assertIn("x", s_dict)
        self.assertIn("y", s_dict)
        self.assertIn("size", s_dict)

    def test_to_dictionary2(self):
        """ Resulting dictionary must be valid """
        s = Square(2, 3, 4, 5)
        s_dict = s.to_dictionary()
        s_res = {"size": 2, "x": 3, "y": 4, "id": 5}

        self.assertTrue(type(s_dict) is dict)
        self.assertDictEqual(s_dict, s_res, "Dictionary are not equal")

    def test_to_update1(self):
        """ `update()` should update all appropriate fields """
        s = Square(2, 3, 4, 5)
        s_dict = s.to_dictionary()
        s_res = {"size": 2, "x": 3, "y": 4, "id": 5}

        self.assertDictEqual(s_dict, s_res, "Dictionary are not equal")

        s.update(6, 5, 4, 3)
        s_dict = s.to_dictionary()
        s_res = {"size": 5, "x": 4, "y": 3, "id": 6}

        self.assertDictEqual(s_dict, s_res, "Dictionary are not equal")

    def test_to_update2(self):
        """ `update()` should accept non-keyworded args """
        s = Square(2, 3, 4, 5)

        new_args = 6, 5, 4, 3
        s.update(*new_args)
        s_dict = s.to_dictionary()
        s_res = {"size": 5, "x": 4, "y": 3, "id": 6}

        self.assertDictEqual(s_dict, s_res, "Dictionary are not equal")

    def test_to_update3(self):
        """ Resulting dictionary must be valid """
        s = Square(2, 3, 4, 5)
        s_dict = s.to_dictionary()
        s_res = {"size": 2, "x": 3, "y": 4, "id": 5}

        self.assertDictEqual(s_dict, s_res, "Dictionary are not equal")

        s.update(27)
        s_dict = s.to_dictionary()
        s_res = {"size": 2, "x": 3, "y": 4, "id": 27}

        self.assertDictEqual(s_dict, s_res, "Dictionary are not equal")

        s.update("Hey")
        s_dict = s.to_dictionary()
        s_res = {"size": 2, "x": 3, "y": 4, "id": "Hey"}

        self.assertDictEqual(s_dict, s_res, "Dictionary are not equal")

    def test_to_update4(self):
        """ field validation are still involved in `update()` """
        s = Square(2, 3, 4, 5)

        with self.assertRaises(ValueError):
            s.update("Hey", -23)

        with self.assertRaises(TypeError):
            s.update("Hey", 23, "x")

        with self.assertRaises(ValueError):
            s.update("Hey", 23, -4, "y")

        with self.assertRaises(TypeError):
            s.update("Hey", 23, 4, "y")

    def test_to_update5(self):
        """ `update()` should keyworded args """
        s1 = Square(2, 3, 4, 5)
        s2 = Square(5, 6, 7, 8)

        s2.update(**s1.to_dictionary())
        self.assertDictEqual(
            s1.to_dictionary(),
            s2.to_dictionary(),
            "Dictionary are not equal"
        )

    def test_to_update6(self):
        """ `update()` should prioritize non-keyword args over
        keyworded args """
        s1 = Square(2, 3, 4, 5)
        s2 = Square(5, 6, 7, 8)
        new_args = 5, 4, 3, 2

        s2.update(*new_args, **s1.to_dictionary())
        self.assertNotEqual(s1.to_dictionary(), s2.to_dictionary())
        s2_res = {"size": 4, "x": 3, "y": 2, "id": 5}
        self.assertEqual(s2.to_dictionary(), s2_res)

    def test_create1(self):
        """ test `create()` """
        s1 = Square(2, 3, 4, 5)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    def test_create2(self):
        """ test `create()` """
        s_dict = {"size": 4, "x": 3, "y": 2, "id": 6}
        s: Square = Square.create(**s_dict)
        self.assertEqual(s_dict, s.to_dictionary())

    def test_create3(self):
        """ test validation `create()` """
        s_dict = {"size": 4, "x": -3, "y": 2, "id": 6}
        with self.assertRaises(ValueError):
            s = Square.create(**s_dict)

    def test_create4(self):
        """ test validation `create()` """
        s_dict = {"size": 0, "x": -1, "y": 2, "id": "Hey"}
        with self.assertRaises(ValueError):
            s = Square.create(**s_dict)

    def test_create5(self):
        """ test validation `create()` """
        s_dict = {"size": "size", "x": 1, "y": 2, "id": "Hey"}
        with self.assertRaises(TypeError):
            s = Square.create(**s_dict)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 5, 5)

        s1_s = [s1, s2]
        Square.save_to_file(s1_s)
        s2_s = Square.load_from_file()

        for s1_, s2_ in zip(s1_s, s2_s):
            self.assertEqual(str(s1_), str(s2_))


if __name__ == '__main__':
    unittest.main()
