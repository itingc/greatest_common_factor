import math
from unittest import TestCase
from app.gcf import GreatestCommonFactor


""" Unit Test the functionality of greatest common factor"""
class TestGcf(TestCase):
    """ Positive number given when initialized(Valid)"""
    def test_init_positive_int(self):
        test_gcf = GreatestCommonFactor("10", "20")
        self.assertEqual(test_gcf.get_x(), 10, "x must be 10")
        self.assertEqual(test_gcf.get_y(), 20, "y must be 20")

    """ Negative number given when initialized(Error)"""
    def test_init_negative_int(self):
         with self.assertRaises(ValueError):
              GreatestCommonFactor("-5", "10")

    """ Float number given when initialized(Error)"""
    def test_init_float(self):
         with self.assertRaises(ValueError):
            GreatestCommonFactor("5.684", "10")

    """ String given when initialized(Error)"""
    def test_init_string(self):
         with self.assertRaises(ValueError):
            GreatestCommonFactor("10", "abc")

    def test_calculate_gcf(self):
        x, y = "4358", "8424"  # even  numbers
        test_gcf = GreatestCommonFactor(x, y)
        self.assertEqual(test_gcf.calculate_gcf(), math.gcd(int(x), int(y)), "Test1:the result isn't correct")

        x, y = "7988465", "8431"  # odd numbers, with larger number at left
        test_gcf = GreatestCommonFactor(x, y)
        self.assertEqual(test_gcf.calculate_gcf(), math.gcd(int(x), int(y)), "Test2:the result isn't correct")

        x, y = "3415", "23469"  # odd numbers, with larger number at right
        test_gcf = GreatestCommonFactor(x, y)
        self.assertEqual(test_gcf.calculate_gcf(), math.gcd(int(x), int(y)), "Test3:the result isn't correct")

        x, y = "31", "199"  # prime numbers
        test_gcf = GreatestCommonFactor(x, y)
        self.assertEqual(test_gcf.calculate_gcf(), math.gcd(int(x), int(y)), "Test4:the result isn't correct")




