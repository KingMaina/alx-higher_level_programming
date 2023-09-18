#!/usr/bin/python3

"""Module containing test cases for the Rectangle class"""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Rectangle test cases"""

    def test_rectangle_no_id(self):
        self.rect1 = Rectangle(5, 10)
        self.assertEqual(self.rect1.id, 1)
    def test_rectangle_id(self):
        self.rect2 = Rectangle(3, 4, id=50)
        self.assertEqual(self.rect2.id, 50)
    def test_rectangle_two
