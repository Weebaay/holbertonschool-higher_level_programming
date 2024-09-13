#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_normal_list(self):
        """Test with a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test with a list containing only one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_repeated_numbers(self):
        """Test with a list of repeated numbers"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_none(self):
        """Test with None as input"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integer_values(self):
        """Test with a list containing non-integer values"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])

if __name__ == "__main__":
    unittest.main()
