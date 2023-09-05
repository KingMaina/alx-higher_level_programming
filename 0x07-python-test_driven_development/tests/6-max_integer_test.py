#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Test cases for max_integer([..])"""
    def test_max_integer(self):
        """Test for max integer"""
        self.assertEqual(max_integer([2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
