#!/usr/bin/python3

"""Module containing test cases for the Rectangle class"""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Rectangle test cases"""
        
    def test_rectangle__id(self):
        """Test that id is set correctly"""
        self.rect1 = Rectangle(5, 10)
        self.assertEqual(self.rect1.id, 1)
    def test_rectangle_with_id(self):
        """Test that id is set correctly when passed in as an argument"""
        self.rect2 = Rectangle(3, 4, id=50)
        self.assertEqual(self.rect2.id, 50)

    def test_rectangle_object_instance(self):
        """Test that object is an instance of Rectangle"""
        self.rect_object = Rectangle(10, 15)
        self.assertIsInstance(self.rect_object, Rectangle)

    def test_rectangle_width_non_int(self):
        """Test that TypeError is raised when width is not an int"""
        with self.assertRaises(TypeError):
            self.rect3 = Rectangle(width="5", height=10)
    def test_rectangle_width_less_than_0(self):
        """Test that ValueError is raised when width is less than 0"""
        with self.assertRaises(ValueError):
            self.neg_rect = Rectangle(width=-5, height=5)
    def test_rectangle_width_0(self):
        """Test that ValueError is raised when width is 0"""
        with self.assertRaises(ValueError):
            self.rect_zero_width = Rectangle(0, 5)

    def test_rectangle_height_non_int(self):
        """Test that TypeError is raised when height is not an int"""
        with self.assertRaises(TypeError):
            self.rect4 = Rectangle(width=5, height="10")
    def test_rectangle_height_less_than_0(self):
        """Test that ValueError is raised when height is less than 0"""
        with self.assertRaises(ValueError):
            self.neg_rect_height = Rectangle(width=5, height=-5)
    def test_rectangle_height_0(self):
        """Test that ValueError is raised when height is 0"""
        with self.assertRaises(ValueError):
            self.rect_zero_height = Rectangle(5, 0)

    def test_rectangle_x_valid(self):
        """Test that x is set correctly"""
        self.rect5 = Rectangle(5, 10, 3)
        self.assertEqual(self.rect5.x, 3)
    def test_rectangle_x_non_int(self):
        """Test that TypeError is raised when x is not an int"""
        with self.assertRaises(TypeError):
            self.rect6 = Rectangle(5, 10, x="3")
    def test_rectangle_x_less_than_0(self):
        """Test that ValueError is raised when x is less than 0"""
        with self.assertRaises(ValueError):
            self.rect7 = Rectangle(5, 10, x=-3)
    
    def test_rectangle_y_valid(self):
        """Test that y is set correctly"""
        self.rect8 = Rectangle(5, 10, 3, 4)
        self.assertEqual(self.rect8.y, 4)
    def test_rectangle_y_non_int(self):
        """Test that TypeError is raised when y is not an int"""
        with self.assertRaises(TypeError):
            self.rect9 = Rectangle(5, 10, 3, y="4")
    def test_rectangle_y_less_than_0(self):
        """Test that ValueError is raised when y is less than 0"""
        with self.assertRaises(ValueError):
            self.rect10 = Rectangle(5, 10, 3, y=-4)

    def test_rectangle_str(self):
        """Test that __str__ method returns correct string representation"""
        self.rect11 = Rectangle(5, 10, 3, 4, 99)
        self.assertEqual(self.rect11.__str__(), "[Rectangle] (99) 3/4 - 5/10")

    def test_rectangle_getter_width(self):
        """Test that width getter works correctly"""
        self.rect12 = Rectangle(5, 10)
        self.assertEqual(self.rect12.width, 5)
    def test_rectangle_getter_height(self):
        """Test that height getter works correctly"""
        self.rect13 = Rectangle(5, 10)
        self.assertEqual(self.rect13.height, 10)
    def test_rectangle_getter_x(self):
        """Test that x getter works correctly"""
        self.rect14 = Rectangle(5, 10, 3)
        self.assertEqual(self.rect14.x, 3)
    def test_rectangle_getter_y(self):
        """Test that y getter works correctly"""
        self.rect15 = Rectangle(5, 10, 3, 4)
        self.assertEqual(self.rect15.y, 4)

    def test_rectangle_setter_width(self):
        """Test that width setter works correctly"""
        self.rect16 = Rectangle(5, 10)
        self.rect16.width = 15
        self.assertEqual(self.rect16.width, 15)
    def test_rectangle_setter_height(self):
        """Test that height setter works correctly"""
        self.rect17 = Rectangle(5, 10)
        self.rect17.height = 15
        self.assertEqual(self.rect17.height, 15)
    def test_rectangle_setter_x(self):
        """Test that x setter works correctly"""
        self.rect18 = Rectangle(5, 10, 3)
        self.rect18.x = 15
        self.assertEqual(self.rect18.x, 15)
    def test_rectangle_setter_y(self):
        """Test that y setter works correctly"""
        self.rect19 = Rectangle(5, 10, 3, 4)
        self.rect19.y = 15
        self.assertEqual(self.rect19.y, 15)

    def test_rectangle_area(self):
        """Test that area method returns correct area"""
        self.rect20 = Rectangle(5, 10)
        self.assertEqual(self.rect20.area(), 50)

    def test_rectangle_display(self):
        """Test that display method prints the rectangle correctly"""
        self.rect21 = Rectangle(5, 10)
        self.rect21.display()
        self.assertEqual(self.rect21.display(), None)

    def test_rectangle_update_args(self):
        """Test that update method updates the rectangle correctly"""
        self.rect22 = Rectangle(5, 10)
        self.rect22.update(99, 2, 3, 4, 5)
        self.assertEqual(self.rect22.__str__(), "[Rectangle] (99) 4/5 - 2/3")

    def test_rectangle_update_kwargs(self):
        """Test that update method updates the rectangle correctly"""
        self.rect23 = Rectangle(5, 10)
        self.rect23.update(id=99, width=2, height=3, x=4, y=5)
        self.assertEqual(self.rect23.__str__(), "[Rectangle] (99) 4/5 - 2/3")

    def test_rectangle_to_dictionary(self):
        """Test that to_dictionary method returns correct dictionary"""
        self.rect24 = Rectangle(5, 10, 3, 4, 99)
        self.assertEqual(self.rect24.to_dictionary(), {'x': 3, 'y': 4, 'id': 99, 'height': 10, 'width': 5})